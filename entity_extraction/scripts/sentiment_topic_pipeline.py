import pandas as pd
import sqlite3
import json
from transformers import pipeline
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from rapidfuzz import fuzz

# ----------------------------------------
# 1. INPUT INLADEN
# ----------------------------------------
print(">> Loading input CSV...")
df = pd.read_csv("../input/ecommerce_feedback.csv")
df = df.dropna(subset=["text"])
texts = df["text"].astype(str).tolist()

# ----------------------------------------
# 2. FUZZY MATCH HELPER
# ----------------------------------------
def fuzzy_contains(text, word, threshold=75):
    text_words = text.lower().split()
    return any(fuzz.ratio(w, word) >= threshold for w in text_words)

# ----------------------------------------
# 3. SENTIMENTMODEL LADEN
# ----------------------------------------
print(">> Loading sentiment model...")
sentiment_model = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# ----------------------------------------
# 4. SENTIMENT FUNCTIE
# ----------------------------------------
def classify_sentiment(text):
    text_lower = text.lower()

    POSITIVE_KAPOT = [
        "kapot goed", "kapot lekker", "kapot fijn", "kapot chill"
    ]
    if any(p in text_lower for p in POSITIVE_KAPOT):
        return "positive", 1.0

    POSITIVE_WORDS = [
        "supersnel", "fantastisch", "geweldig", "topservice",
        "perfect", "aanrader", "supergoed", "topkwaliteit",
        "heerlijk", "blij", "tevreden"
    ]
    for w in POSITIVE_WORDS:
        if fuzzy_contains(text_lower, w):
            return "positive", 0.9

    NEGATIVE_WORDS = [
        "gedoe", "foutmelding", "waardeloos", "dramatisch",
        "slecht", "te lang", "belachelijk", "superchagrijnig",
        "gevaarlijk", "irritant", "niet goed", "werkt niet",
        "niet geleverd", "kapot", "beschadigd", "klote",
        "stuk", "defect", "mislukt", "teleurgesteld"
    ]
    for w in NEGATIVE_WORDS:
        if fuzzy_contains(text_lower, w):
            return "negative", 0.1

    try:
        result = sentiment_model(text[:512])[0]
        label = result["label"].lower()
        score = float(result["score"])

        if "1" in label or "2" in label:
            return "negative", score
        if "3" in label:
            return "neutral", score
        if "4" in label or "5" in label:
            return "positive", score

        return "neutral", score
    except:
        return "neutral", 0.0

print(">> Running sentiment classification...")
sentiments = [classify_sentiment(t) for t in texts]
df["sentiment_label"] = [s[0] for s in sentiments]
df["sentiment_score"] = [s[1] for s in sentiments]

# ----------------------------------------
# 5. ASPECT DETECTION
# ----------------------------------------
ASPECT_KEYWORDS = {
    "delivery": ["bezorging", "bezorger", "bezorgd", "pakket"],
    "customer_service": ["klantenservice", "medewerker", "telefonisch"],
    "product_quality": ["kwaliteit", "kapot", "defect", "beschadigd"],
    "price": ["prijs", "korting", "duur", "goedkoop"],
    "website": ["website", "site", "checkout", "inloggen"],
    "returns": ["retour", "terugsturen", "refund"]
}

def detect_aspects(text):
    text_lower = text.lower()
    matched = []
    for asp, kws in ASPECT_KEYWORDS.items():
        if any(kw in text_lower for kw in kws):
            matched.append(asp)
    return ",".join(matched) if matched else "none"

print(">> Detecting aspects...")
df["aspects"] = df["text"].astype(str).apply(detect_aspects)

# ----------------------------------------
# 6. TOPIC MODELING (BERTopic)
# ----------------------------------------
print(">> Loading embedding model...")
embedding_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

print(">> Fitting BERTopic...")
topic_model = BERTopic(
    embedding_model=embedding_model,
    language="multilingual",
    calculate_probabilities=True,
    verbose=True
)

topics, probs = topic_model.fit_transform(texts)
df["topic_id"] = topics
topic_info = topic_model.get_topic_info()

# ----------------------------------------
# 7. OUTPUT OPSLAAN (CSV + SQLite)
# ----------------------------------------
print(">> Saving CSVs...")
df.to_csv("../output/ecommerce_feedback_enriched.csv", index=False)
topic_info.to_csv("../output/ecommerce_topics.csv", index=False)

print(">> Saving SQLite database...")
for col in topic_info.columns:
    topic_info[col] = topic_info[col].apply(
        lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x
    )

con = sqlite3.connect("../database/ecommerce_nlp.db")
df.to_sql("feedback", con, index=False, if_exists="replace")
topic_info.to_sql("topics", con, index=False, if_exists="replace")
con.close()

print(">> DONE. All data saved successfully.")

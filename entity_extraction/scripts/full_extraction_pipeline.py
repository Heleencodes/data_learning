import spacy
import re
import pandas as pd
import sqlite3

# Load spaCy
nlp = spacy.load("en_core_web_sm")

# Load text
with open("../input/raw_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Regex patterns
patterns = {
    "phones": r"(?:\+31|0)[\s-]?(6[\s-]?\d{8})",
    "emails": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "addresses": r"\b[A-Z][a-z]+\s+\d+,\s+\d{4}\s[A-Z]{2}\s+[A-Z][a-z]+"
}

regex_results = {k: re.findall(v, text) for k, v in patterns.items()}

# spaCy NER
doc = nlp(text)

persons = []
dates = []
locations = []
organizations = []

for ent in doc.ents:
    if ent.label_ == "PERSON":
        persons.append(ent.text)
    elif ent.label_ == "DATE":
        dates.append(ent.text)
    elif ent.label_ == "GPE":
        locations.append(ent.text)
    elif ent.label_ == "ORG":
        organizations.append(ent.text)

# Build DataFrame
df = pd.DataFrame({
    "person": pd.Series(persons),
    "date": pd.Series(dates),
    "location": pd.Series(locations),
    "organization": pd.Series(organizations),
    "email": pd.Series(regex_results["emails"]),
    "phone": pd.Series(regex_results["phones"]),
    "address": pd.Series(regex_results["addresses"])
})

# Save intermediary CSV
df.to_csv("../output/entities_full.csv", index=False)

# Save to database
con = sqlite3.connect("../database/entities_full.db")
df.to_sql("entities", con, index=False, if_exists="replace")
con.close()

print("✔️ Full pipeline completed. Database saved to /database/entities_full.db")

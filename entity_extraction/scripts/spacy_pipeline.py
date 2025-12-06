import spacy
import pandas as pd
import sqlite3

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load raw text
with open("../input/raw_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Process with spaCy
doc = nlp(text)

persons = []
locations = []
dates = []
organizations = []

for ent in doc.ents:
    if ent.label_ == "PERSON":
        persons.append(ent.text)
    elif ent.label_ == "GPE":
        locations.append(ent.text)
    elif ent.label_ == "DATE":
        dates.append(ent.text)
    elif ent.label_ == "ORG":
        organizations.append(ent.text)

# Convert to DataFrames
df_people = pd.DataFrame({"person": persons})
df_locations = pd.DataFrame({"location": locations})
df_dates = pd.DataFrame({"date": dates})
df_orgs = pd.DataFrame({"organization": organizations})

# Save interim CSVs
df_people.to_csv("../output/people_spacy.csv", index=False)
df_locations.to_csv("../output/locations_spacy.csv", index=False)
df_dates.to_csv("../output/dates_spacy.csv", index=False)
df_orgs.to_csv("../output/organizations_spacy.csv", index=False)

# Save to SQLite
con = sqlite3.connect("../database/entities_spacy.db")

df_people.to_sql("people", con, index=False, if_exists="replace")
df_locations.to_sql("locations", con, index=False, if_exists="replace")
df_dates.to_sql("dates", con, index=False, if_exists="replace")
df_orgs.to_sql("organizations", con, index=False, if_exists="replace")

con.close()

print("✔️ spaCy pipeline completed. Database saved to /database/entities_spacy.db")

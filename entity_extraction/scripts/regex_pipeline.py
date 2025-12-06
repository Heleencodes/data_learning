import re
import pandas as pd
import sqlite3

# ----------------------------------------------------
# Load raw text
# ----------------------------------------------------
with open("../input/raw_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ----------------------------------------------------
# Regex patterns
# ----------------------------------------------------
patterns = {
    "names": r"\b[A-Z][a-z]+(?:\s(?:de\s|van\s|van de\s|van der\s)?[A-Z][a-z]+)+",
    "phones": r"(?:\+31|0)[\s-]?(6[\s-]?\d{8})",
    "emails": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "dates": r"\b\d{1,2}\s(?:januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december)\s\d{4}\b",
    "times": r"\b\d{1,2}:\d{2}\b",
    "addresses": r"\b[A-Z][a-z]+\s+\d+,\s+\d{4}\s[A-Z]{2}\s+[A-Z][a-z]+"
}

# Extract entities
extracted = {key: re.findall(pattern, text) for key, pattern in patterns.items()}

# ----------------------------------------------------
# Convert to DataFrames
# ----------------------------------------------------
df_people = pd.DataFrame({"name": extracted["names"]})
df_contacts = pd.DataFrame({
    "phone": extracted["phones"],
    "email": extracted["emails"]
})
df_appointments = pd.DataFrame({
    "date": extracted["dates"],
    "time": extracted["times"] if extracted["times"] else [None]
})
df_addresses = pd.DataFrame({"address": extracted["addresses"]})

# Save interim CSV (optional)
df_people.to_csv("../output/people_regex.csv", index=False)
df_contacts.to_csv("../output/contacts_regex.csv", index=False)
df_appointments.to_csv("../output/appointments_regex.csv", index=False)
df_addresses.to_csv("../output/addresses_regex.csv", index=False)

# ----------------------------------------------------
# Save to SQLite database
# ----------------------------------------------------
con = sqlite3.connect("../database/entities_regex.db")

df_people.to_sql("people", con, index=False, if_exists="replace")
df_contacts.to_sql("contacts", con, index=False, if_exists="replace")
df_appointments.to_sql("appointments", con, index=False, if_exists="replace")
df_addresses.to_sql("addresses", con, index=False, if_exists="replace")

con.close()

print("✔️ Regex pipeline completed. Database saved to /database/entities_regex.db")

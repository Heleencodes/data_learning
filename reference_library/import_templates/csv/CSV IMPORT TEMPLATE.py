import pandas as pd
import numpy as np

# === 1. Filepath ===
# Gebruik direct de URL of een lokaal pad.
filepath = "URL_HIER"

# === 2. Column names (alleen gebruiken als IBM/ADA deze apart meestuurt) ===
headers = [
    # "col1", "col2", "col3", ...
]

# === 3. DataFrame inladen ===
try:
    if headers:
        df = pd.read_csv(filepath, header=None, na_values=["?", "NA", "NaN"])
        df.columns = headers
    else:
        df = pd.read_csv(filepath, na_values=["?", "NA", "NaN"])

except FileNotFoundError:
    print("❌ Het bestand is niet gevonden. Controleer het pad of de URL.")
except pd.errors.ParserError:
    print("❌ CSV kon niet worden gelezen — controleer het formaat.")
else:
    # === 4. Eerste checks ===
    print("\n=== Dataset succesvol geladen ===")
    print("Shape:", df.shape)
    print("\n--- Eerste 5 rijen ---")
    display(df.head())
    print("\n--- Informatie over DataFrame ---")
    df.info()



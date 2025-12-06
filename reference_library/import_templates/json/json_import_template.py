import pandas as pd

# === 1. Filepath ===
filepath = "data.json"

# === 2. Load JSON ===
# Works for records, list of dicts, or nested JSON with orient="records"
df = pd.read_json(filepath)

# === 3. Checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

import pandas as pd

# === 1. Filepath ===
filepath = "data.parquet"

# === 2. Load parquet ===
df = pd.read_parquet(filepath)

# === 3. Checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

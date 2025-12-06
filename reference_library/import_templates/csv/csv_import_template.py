import pandas as pd

# === 1. Filepath ===
filepath = "URL_OF_FILE_OR_LOCAL_PATH"

# === 2. Optional column names ===
headers = [
    # "col1", "col2", ...
]

# === 3. Load CSV ===
if len(headers) > 0:
    df = pd.read_csv(filepath, header=None)
    df.columns = headers
else:
    df = pd.read_csv(filepath)

# === 4. Basic checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

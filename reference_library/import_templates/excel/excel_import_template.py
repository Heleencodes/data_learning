import pandas as pd

# === 1. Filepath ===
filepath = "FILE.xlsx"

# === 2. Sheet name ===
sheet = "Sheet1"  # or index (0, 1, 2...)

# === 3. Load Excel ===
df = pd.read_excel(filepath, sheet_name=sheet)

# === 4. Checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

import sqlite3
import pandas as pd

# === 1. Database pad ===
db_path = "PATH_TO_DATABASE.db"

# === 2. Query ===
query = """
SELECT *
FROM your_table
LIMIT 10;
"""

# === 3. Connectie ===
conn = sqlite3.connect(db_path)

# === 4. Query naar DataFrame ===
df = pd.read_sql_query(query, conn)

# === 5. Checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

# === 6. Sluit verbinding ===
conn.close()

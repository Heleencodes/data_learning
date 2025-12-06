from sqlalchemy import create_engine
import pandas as pd

# === 1. Connection string ===
# Voorbeelden:
# engine = create_engine("sqlite:///your.db")
# engine = create_engine("mysql+pymysql://user:pw@host:3306/dbname")
# engine = create_engine("postgresql://user:pw@host:5432/dbname")

connection_string = "sqlite:///PATH_TO_DATABASE.db"
engine = create_engine(connection_string)

# === 2. Query ===
query = """
SELECT *
FROM your_table
LIMIT 10;
"""

# === 3. DataFrame ===
df = pd.read_sql(query, engine)

# === 4. Checks ===
print("Shape:", df.shape)
print(df.head())
df.info()

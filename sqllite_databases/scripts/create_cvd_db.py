import sqlite3
conn = sqlite3.connect(r"C:/Users/Beheerder/data_learning/sql/cvd.db")
conn.execute("CREATE TABLE IF NOT EXISTS test123 (id INTEGER);")
conn.close()

print("Database aangemaakt!")

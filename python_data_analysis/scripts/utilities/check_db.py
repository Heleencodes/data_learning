import sqlite3

try:
    conn = sqlite3.connect("cvd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tabellen gevonden:", tables)
except Exception as e:
    print("FOUT:", e)
finally:
    conn.close()

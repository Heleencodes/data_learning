import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
);
""")

cursor.execute("INSERT INTO employees (name, salary) VALUES ('Sophie', 3300)")
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Mark', 5100)")
cursor.execute("INSERT INTO employees (name, salary) VALUES ('Layla', 4200)")

connection.commit()
connection.close()

print("✅ Database test.db aangemaakt!")

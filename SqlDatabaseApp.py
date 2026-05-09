import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT)")
cur.execute("INSERT INTO users VALUES ('Samarth')")
conn.commit()
conn.close()
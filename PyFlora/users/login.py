import sqlite3

conn = sqlite3.connect('PyFlora/users/users.db')


cursor = conn.cursor()

cursor.execute("SELECT * FROM user")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

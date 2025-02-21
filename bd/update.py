import sqlite3

connection = sqlite3.connect('title.db')
cursor = connection.cursor()

id = 1
cursor.execute("UPDATE movies SET score = ? WHERE id = ?", (8.5, id))

connection.commit()
connection.close()
print()
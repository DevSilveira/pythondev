import sqlite3

connection = sqlite3.connect('title.db')
cursor = connection.cursor()

data = cursor.execute("SELECT * FROM movies")

print(data.fetchall())

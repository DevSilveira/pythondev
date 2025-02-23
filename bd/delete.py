import sqlite3

# Connecting in database
connection = sqlite3.connect("title.db")
cursor = connection.cursor()

# Removing data from database
id = (1, 3)
cursor.execute("DELETE FROM movies WHERE id IN (?, ?)", id)

connection.commit()

print("Dados removidos!")

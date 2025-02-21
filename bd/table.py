import sqlite3

# Connecting in DB
connection = sqlite3.connect('title.db')

# Creating cursor
cursor = connection.cursor()

# Creating table
cursor.execute(
    """
        CREATE TABLE movies(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            score REAL NOT NULL
        );
    """
)

# Closing connection
connection.close()
print()
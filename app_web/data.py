import sqlite3

def connect_db():
    connection = sqlite3.connect("movies.db")
    return connection

def insert_data(name, year, score):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        """
            INSERT INTO title(name, year, score)
            VALUES(?, ?, ?)
        """,
        (name, year, score)
    )
    connection.commit()
    connection.close()

def get_data():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM title")
    data = cursor.fetchall()
    cursor.close()
    return data
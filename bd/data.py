import sqlite3

# Connecting DB
connection = sqlite3.connect('title.db')
cursor = connection.cursor()

cursor.execute(
    """
        INSERT INTO movies(name, year, score) 
        VALUES('Sonic', 2020, 8.0)
    """
)

# cursor.execute(
#     """
#         DELETE FROM movies WHERE id = 2
#     """
# )

connection.commit()
connection.close()
print("Dados foram inseridos!")
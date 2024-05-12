import mysql.connector

conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "board-games-collection"
        )
cursor = conn.cursor()

username = "dummy1"
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))

res = cursor.fetchone()

print(res)

cursor.close()
conn.close()
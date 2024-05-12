import mysql.connector

class SQL_Connector:
    def __init__(self, host: str = "localhost", user: str = "root", password: str = "", database: str = "board-games-collection") -> None:
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor()


    def execute_query(self, query: str):
        self.cursor.execute(query)
        

    def fetchall_query(self, query: str, values: tuple) -> list:
        
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()

        return result
    

    def fetchone_query(self, query: str, values: tuple) -> tuple:
        
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        
        return result

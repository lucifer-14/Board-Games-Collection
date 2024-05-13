import mysql.connector
import utils.config_handler as CONF_H

conf_h = CONF_H.Config_Handler()

DATABASE_NAME=conf_h.get_config("DATABASE_NAME")
DATABASE_HOST=conf_h.get_config("DATABASE_HOST")
DATABASE_PORT=int(conf_h.get_config("DATABASE_PORT"))
DATABASE_USER=conf_h.get_config("DATABASE_USER")
DATABASE_PASSWORD=conf_h.get_config("DATABASE_PASSWORD")
DATABASE_TIMEZONE=conf_h.get_config("DATABASE_TIMEZONE")

class SQL_Connector:
    def __init__(self, host: str = DATABASE_HOST, 
                user: str = DATABASE_USER,
                password: str = DATABASE_PASSWORD, 
                database: str = DATABASE_NAME,
                timezone: str = DATABASE_TIMEZONE) -> None:
        
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            use_pure = True,
        )
        
        self.cursor = self.conn.cursor()


    def execute_query(self, query: str):
        
        self.cursor.execute(query)
        self.cursor.close()
        self.conn.close()
        

    def fetchall_query(self, query: str, values: tuple) -> list:
        
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()

        self.cursor.close()
        self.conn.close()

        return result
    

    def fetchone_query(self, query: str, values: tuple) -> tuple:
        
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()
        
        return result
    
    def insert_query(self, query:str, values: tuple) -> None:
        self.cursor.execute(query, values)
        self.conn.commit()

        self.cursor.close()
        self.conn.close()
    

    def update_query(self, query: str, values: tuple) -> None:
        
        self.cursor.execute(query, values)
        self.conn.commit()

        self.cursor.close()
        self.conn.close()


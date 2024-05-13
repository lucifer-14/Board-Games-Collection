import socket_handle.send_request as S_REQ
import crypto_custom.bcrypt.bcrypter as bcrypter
import sql_handle.sql_connector as SQLC

class Register():
    def __init__(self, username: str, email:str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = password
        self.data = {"username": self.username, "email": self.email, "password": self.password, }
        

    def register_request(self) -> dict:
        """ Client side register request, sends request then receives response
        """
        SR = S_REQ.Send_Request()
        response = SR.send_req("POST", "/register", self.data)
        response_code = response['response-code']
        response_comment = response['response-comment']
        response_data = response['data']

        return response_data
    

    def register_response(self) -> dict:
        """ Server side register response, generates response
        """

        response_code = 200
        response_comment = "Success"
        
        bcrypt = bcrypter.bcrypter()
        hashed_pass = bcrypt.crypt(self.password)

        sql_connection = SQLC.SQL_Connector()
        query = "INSERT INTO users(username, email, hashed_password) VALUES(%s, %s, %s)"
        values = (self.username, self.email, hashed_pass)

        sql_connection.insert_query(query, values)

        response_data = {"is_register_success": True,
                         "comment": "Registration success! Please Login."}
    

        full_response_data = {"response-code": response_code, 
                            "response-comment": response_comment,
                            "data": response_data}
        
        return full_response_data


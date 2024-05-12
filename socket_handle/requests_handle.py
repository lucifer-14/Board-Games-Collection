"""
This is server-side
"""
import socket
import json
import socket_handle.auth_handle.login as SAL
import sql_handle.sql_connector as SQLC

class Requests_Handle:
    def __init__(self, conn: socket.socket) -> None:
        self.conn = conn
        # while True:
        # full_data = b""
        # while True:
            # print("reconstructing....")
            # data = conn.recv(1)
            # if not data:
            #     break
            # full_data += data
        # if not full_data:
        #     break
        print("reconstructing....")
        full_data = conn.recv(4096)

        print(full_data.decode('utf-8'))
        req_full_data = json.loads(full_data.decode('utf-8'))

        self.req_type = req_full_data['request-type']
        self.req_uri = req_full_data['request-URI']
        self.req_data = req_full_data['data']

        if self.req_uri == "/login":
            self.login_handle()

        conn.close()


    def login_handle(self) -> None:
        
        response_code = 200
        response_comment = "Success"
        
        sql_connection = SQLC.SQL_Connector()
        query = "SELECT * FROM users WHERE username= %s"
        search = (self.req_data['username'],)

        res = sql_connection.fetchone_query(query, search)

        if res:
            true_password = res[2]

            login_handle = SAL.Login(self.req_data['username'], self.req_data['password'])
            login_handle_verify_res = login_handle.login_verify(true_password)
            
            response_data = {"is_login_success": login_handle_verify_res}

            if login_handle_verify_res:
                response_data.update({"comment": "Login success!"})
            else:
                response_data.update({"comment": "Login failed!"})

        else:
            response_data = {"is_login_success": False, "comment": "Login failed!"}
    

        full_response_data = {"response-code": response_code, 
                            "response-comment": response_comment,
                            "data": response_data}
        
        full_response_data = json.dumps(full_response_data)

        self.conn.send(full_response_data.encode('utf-8'))
        

    def register_handle(self):
        pass
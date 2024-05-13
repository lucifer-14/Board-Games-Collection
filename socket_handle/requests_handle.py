"""
This is server-side
"""
import socket
import json
import socket_handle.auth_handle.login as SAL
import socket_handle.auth_handle.register as SAR


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
        print("receiving request....")
        full_data = conn.recv(4096)

        print(full_data.decode('utf-8'))
        req_full_data = json.loads(full_data.decode('utf-8'))

        self.req_type = req_full_data['request-type']
        self.req_uri = req_full_data['request-URI']
        self.req_data = req_full_data['data']

        if self.req_uri == "/login":
            self.login_handle()

        if self.req_uri == "/register":
            self.register_handle()

        conn.close()
        print("[+] Connection terminated.")


    def login_handle(self) -> None:

        login_handle = SAL.Login(username=self.req_data['username'], 
                                 password=self.req_data['password'])
        
        full_response_data = login_handle.login_response()
        
        full_response_data = json.dumps(full_response_data)

        self.conn.send(full_response_data.encode('utf-8'))
        

    def register_handle(self):
        
        register_handle = SAR.Register(username=self.req_data['username'],
                                       email=self.req_data['email'],
                                       password=self.req_data['password'])
        
        full_response_data = register_handle.register_response()

        full_response_data = json.dumps(full_response_data)

        self.conn.send(full_response_data.encode('utf-8'))
""" 
This is client-side
"""

import socket
import json
import socket_handle.establish_connection as ESTA_CONN

class Send_Request:
    def __init__(self):
        
        esta = ESTA_CONN.Establish_Connection()
        self.conn = esta.esta_conn()

    def send_req(self, req_type: str, req_uri: str, data: dict) -> dict:
        full_data = {"request-type": req_type,
                     "request-URI": req_uri,
                     "data": data}
        full_data = json.dumps(full_data)
        # print(self.conn)
        # print(type(self.conn))
        self.conn.sendall(full_data.encode('utf-8'))
        print("data sent from client")
        
        # return_data = b""
        # while True:
            # print("reconstructing....")
            # data = self.conn.recv(1)
            # if not data:
                # break
            # return_data += data
        print("receiving response....")
        
        return_data = self.conn.recv(4096)
        print(return_data.decode('utf-8'))
        
        self.conn.close()
        print("[+] Connection terminated (client-side).")
        

        return json.loads(return_data.decode('utf-8'))
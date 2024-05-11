import socket
from auth_handle import login

class Requests_Handle:
    def __init__(self, conn) -> None:
        self.conn = conn
        while True:
            full_data = b""
            while True:
                print("reconstructing....")
                data = conn.recv(1)
                if not data:
                    break
                full_data += data
            if not full_data:
                break

            print(full_data.decode('utf-8'))

    def login_handle(self):
        pass

    def register_handle(self):
        pass
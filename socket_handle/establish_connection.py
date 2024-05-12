import socket

class Establish_Connection:
    def __init__(self, HOST: str = "127.0.0.1", PORT: int = 14141):
        self.HOST = HOST
        self.PORT = PORT


    def esta_conn(self) -> socket.socket:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
            
        return s
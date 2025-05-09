import socket
import threading
import signal
import sys
import utils.config_handler as CONF_H
from socket_handle.requests_handle import Requests_Handle


class Server:
    def __init__(self, HOST: str = '127.0.0.1', PORT: int = 14141) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.conn_list = []
        self.thread_list = []
        

    def serv(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.bind((self.HOST, self.PORT))
            soc.listen()
            print(f"[+] Server listening on {self.HOST}:{self.PORT}")
            while True:
                conn, addr = soc.accept()
                print(f"[+] New Connection: {conn}")
                self.conn_list.append(conn)
                
                print("[+] Connection handler initiated...")
                thread = threading.Thread(target=self.handle_connection, args=(conn,))
                self.thread_list.append(thread)
                thread.start()

    def handle_connection(self, conn) -> None:
        Requests_Handle(conn)
        



if __name__ == "__main__":
    # Remove Later 
    def sigint_handler(sig, frame):
        print("\nServer stopped")
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint_handler)
    # up to here

    conf_h = CONF_H.Config_Handler()

    APP_SERVER_HOST = conf_h.get_config("APP_SERVER_HOST")
    APP_SERVER_PORT = int(conf_h.get_config("APP_SERVER_PORT"))

    server = Server(APP_SERVER_HOST, APP_SERVER_PORT)
    server.serv()
    print(server.conn_list)
            
        
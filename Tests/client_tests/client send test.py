import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 14141))
    while True:
        data = input("message: ")
        s.send(data.encode('UTF-8'))

        s.close()
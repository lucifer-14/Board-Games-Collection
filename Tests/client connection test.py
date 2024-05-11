import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect_ex(('127.0.0.1', 14141))

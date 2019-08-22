import socket
import sys 

HOST = '192.168.178.31'  # The server's hostname or IP address
PORT = 65432             # The port used by the server

msg = sys.argv[1].encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(msg))
    data = s.recv(1024)

print('Received', data.decode())
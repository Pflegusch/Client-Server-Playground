import socket
import sys 

HOST = sys.argv[1]
PORT = (int)(sys.argv[2])
msg = sys.argv[3].encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(msg))
    data = s.recv(1024)

print('Received', data.decode())
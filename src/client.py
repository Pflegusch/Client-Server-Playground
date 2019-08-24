import socket
import sys 

args = sys.argv[1].split(':')
host = args[0]
port = (int)(args[1])
msg = sys.argv[2].encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(bytes(msg))
    data = s.recv(1024)

print('Received:', data.decode())
import socket
import sys 

# args = sys.argv[1].split(':')
# host = args[0]
# port = (int)(args[1])
# msg = sys.argv[2].encode()
msg = sys.argv[0].encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.178.31", 33333))
    s.sendall(bytes(msg))
    data = s.recv(1024)

print('Received:', data.decode())
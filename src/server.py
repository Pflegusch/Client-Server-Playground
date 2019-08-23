import socket
import os

HOST = '192.168.178.31'  # Standard loopback interface address (localhost)
PORT = 65432             # Port to listen on (non-privileged ports are > 1023)

while True: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server started on " + str(HOST) + ":" + str(PORT))
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:               
                data = conn.recv(1024)
                if data == b'exit': 
                    conn.sendall(b'Server shutdown')
                    print("Client initiated shutdown")
                    exit() 
                elif data == b'sleep': 
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    conn.sendall(b'Server set to sleep')
                    exit()
                if not data:
                    break
                else: 
                    print(data.decode())
                    conn.sendall(b'Server received message') 
                    exit()
                conn.sendall(data)
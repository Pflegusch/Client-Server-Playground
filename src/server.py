from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import socket
import os
import sys

import pytest

def basic_test():
    assert(1==1)

HOST = '192.168.178.31'  # Standard loopback interface address (localhost)
PORT = (int)(sys.argv[1])

if PORT <= 1023 or PORT >= 65535: 
    print("ERROR: Please choose a valid Port ranging from 1024 to 65535") 
    exit() 

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
                elif b'vol'in data:
                    try: 
                        import re
                        vol = int(re.search(r'\d+', data.decode()).group(0)) 
                        sessions = AudioUtilities.GetAllSessions()
                        for session in sessions:
                            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                            if session.Process and session.Process.name() == "Spotify.exe":
                                print("Spotify volume: %s" % (volume.GetMasterVolume() * 100))
                                volume.SetMasterVolume(vol / 100, None)
                        conn.sendall(b'Spotify master volume successfully adjusted!')
                        exit() 
                    except: 
                        print("Unknown Error occurred") 
                        conn.sendall(b'Unknown error occured') 
                        exit() 
                if not data:
                    break
                else: 
                    print(data.decode())
                    conn.sendall(b'Server received message') 
                    exit()
                conn.sendall(data)
import pytest
import socket

def test_start_server(HOST='localhost', PORT=65333): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        assert(s is not None)

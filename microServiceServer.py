
from socket import *
import json

HOST = "localhost"
PORT = 8000

with socket(AF_INET, SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    connectedServer, address = serverSocket.accept()

    with connectedServer:
        print(f"Success! You are connected with: {address}")

        while True:
            data = connectedServer.recv(1024)
            if not data:
                print("Connection not successful...")
                break
            connectedServer.sendall(data)
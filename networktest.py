#!/usr/bin/python

import socket

SRV_ADDR = "127.0.0.1"#input("server IP: ")
SRV_PORT = 15782#input("server socket: ")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((SRV_ADDR,SRV_PORT))

print("Server started! Waiting for connections....")
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection, address = s.accept()
print("Client connect with address: ",address)

while 1:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(b'-- Message Received --\n')
    print(data.decode('utf-8'))
connection.close()

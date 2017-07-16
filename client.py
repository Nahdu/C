#!/usr/bin/python

#a simple Python client to start with network programming
import socket

#setting address and port number to connect to
address = "10.0.2.15"
port = 15782

#create a socket
s = socket.socket()

#bind socket to address and port
s.connect((address,port))

#send a message
s.send(b'Brackets never go on the same line as the iterational or conditional structure')

#let user secify a message to send
message = input("enter a message to send: ")

#encode the message with utf then as bytes then convert to an array of bytes
message = bytes(message.encode('utf-8'))

#send the user string to the server
s.send(message)

#read message from the server
print("Server says: ", s.recv(1024).decode('utf-8'))

#close the connection
print("\nClosing connection")
s.close()

#!/usr/bin/python

import socket


#Setting server address and port number
SRV_ADDR = "10.0.2.15"#input("server IP: ")
SRV_PORT = 15782#input("server socket: ")


#Creating a socket object
#AF_INET indicates the socket family which determins the format of the address used for binding, AF_INET indicates and address in the form (host,port)
#SOCK_STREAM is the socket type. A stream socket is used for TCP socket, 
#DGRAM would be used for UDP and RAW for directly accessing an IP protocol.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding the above socket object to address and port number
s.bind((SRV_ADDR,SRV_PORT))

#telling the socket to listen for connections
s.listen(1)

print("Server started! Waiting for connections....\n")

#Accept the first connection
connection, address = s.accept()

print("Client connect with address: ",address,"\n")

#Print message received and play messages back
try:
    while 1:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(b'-- Message Received --\n')
        print("Client sent: ", data.decode('utf-8'))
except ConnectionResetError:
    print("Connection closed by client. Exiting now")

#close the connection
s.close()

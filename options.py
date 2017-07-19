#!/usr/bin/python

#small program to explore the HTTP options command

import http.client

#set target
host = "example.com"
port = 80

try:
    #open a connection and send and OPTIONS request
    connection = http.client.HTTPConnection(host,port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    print("Enabled methods are: ",response.getheader('allow'))
    connection.close()

    #open a connection send a GET request for /"
    print("Sending GET request for /")
    connection = http.client.HTTPConnection("example.com",80)
    connection.request('GET','/')
    print("GET response status:", str(connection.getresponse().status))

    connection.close()
except ConnectionRefusedError:
    print("Connection refused")

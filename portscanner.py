#!/usr/bin/python

import socket

#setting parameters
target = "198.105.254.228"
low_port = 1
high_port = 10


print("Scanning", target, "from ports", str(low_port), "to", str(high_port))

#note that the range function is not inclusive
for port in range(low_port,high_port):
    #creating a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #settting timeout to not make this slow as hell
    s.settimeout(1)

    #connect to specified socket and see if connection opens
    status = s.connect_ex((target,port))
    
    #checking statuis
    if(status == 0):
        print("Port:", port, "is OPEN")
    else:
        print("Port:", port, "is CLOSED")

    #close the port when the scanning is complete
    s.close()


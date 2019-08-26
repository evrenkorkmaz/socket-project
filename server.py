# -*- coding: utf-8 -*-
import socket
import os
import time

a = 0
while True:
    if os.path.exists("/tmp/python_unix_sockets_example"): # check a socket path
        os.remove("/tmp/python_unix_sockets_example")  # if exist remove that socket

    print("Opening socket...")
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) # create a server socket for connections
    server.bind("/tmp/python_unix_sockets_example")

    print("Listening...")

    while True:
        datagram = server.recv(1024)  # wait a message from server.py
        if not datagram:
            break
        else:
            print("-" * 20)
            print(datagram.decode('utf-8')) #print a message
            if "DONE" == datagram.decode('utf-8'):  # check Done message
                break
            if "end" == datagram.decode('utf-8'): # check END message
                a = 2
                break
    if a == 2:
        break
    time.sleep(1) # wait a create socket from client.py
    server.connect("/tmp/python_unix_sockets_example")

    while True:
        try:
            x = input("> ")  #enter a message
            if "" != x:
                print("Send:", x)
                server.send(x.encode('utf-8')) #send message
                if "DONE" == x: # "DONE" message test
                    print("Shutting Down")
                    break
                if "END" == x:
                    print("END")
                    a = 1 # break loop
                    server.close() #close socket connection
                    break
        except KeyboardInterrupt as k:
            print("Shutting down.")
            break
    if a == 1:
        break
print("-" * 20)
print("Shutting down...")
server.close()
os.remove("/tmp/python_unix_sockets_example")

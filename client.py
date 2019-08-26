# -*- coding: utf-8 -*-
import socket
import os
import time
a=0 # for the break loop
while True:
   print("Connecting...")
   time.sleep(2) # waiting for a server.py create a socket 
   if os.path.exists("/tmp/python_unix_sockets_example"): # check a socket path
       client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) # create a client socket for connections
       client.connect("/tmp/python_unix_sockets_example") # connections
       print("Ready.") 
       print("Ctrl-C or write 'END' to quit.")
       print("Sending 'DONE' end of the conversation on the client side and wait the message to server")
       while True:
           try:
               x = input("> ") # input a message from user
               if "" != x: # check empty mesaage
                   print("SEND:", x) 
                   client.send(x.encode('utf-8')) # sending a message to server socket
                   if "DONE" == x: # Sending 'DONE' end of the conversation on the client side and wait the message to server
                       print("DONE")
                       break
                   if "END"==x: # Sending "END" for the close socket.
                       print("END")
                       a=1
                       client.close() # close socket connection
                       break
           except KeyboardInterrupt as k: 
               print("END")
               client.close()
               break
       if a==1:
           break
# If user sending "DONE" client.pt close the socket connection
# End then know client.py create a socket for the server.py connection

       if os.path.exists("/tmp/python_unix_sockets_example"): #check a socket path exist
           os.remove("/tmp/python_unix_sockets_example") # if exist remove that socket
       client.bind("/tmp/python_unix_sockets_example") # and create a socket for server.py connetcion
       while True:
           datagram = client.recv(1024) # wait a message from server.py
           if not datagram:
               break
           else:
               print("-" * 20)
               print(datagram.decode('utf-8')) #print a message
               if "DONE" == datagram.decode('utf-8'): # check Done message
                   break
               if "END" == datagram.decode('utf-8'): # check END message
                   a = 2
                   break
       if a==2:
           break
   else:
       print("Couldn't Connect!")
   print("Done")
   client.close() # close socket connection

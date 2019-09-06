## Simple Socket Message Project

This project is a simple message project with using unix socket

## Usage

Fist run the server.py for the create socket file. And run client.py. First only client.py can send a message to server.py until sending DONE message. When client.py sending DONE mesaage, close the socket on server.py. After that client.py create a socket and server.py connect the soket on client.py. Shotly when client.py send a DONE message, client run like server, server run like client. If anyone send END message, programs closing.

# https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/

import socket

ClientSocket = socket.socket()
host = '98.37.193.32'
port = 1200

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
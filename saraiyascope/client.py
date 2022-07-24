# https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/
# runs on the raspberry pi
# deprecated --> see sensors.py in top directory

import socket

ClientSocket = socket.socket()
host = '10.0.0.211' # ip address of displaying computer
# host = 'Tuethus-MacBook-Pro.local' # ip address of displaing computer
port = 1234

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    exit(1)

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    # ClientSocket.sendall(str.encode(Input))
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
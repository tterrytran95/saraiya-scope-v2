# https://codezup.com/socket-server-with-multiple-clients-model-multithreading-python/
# runs on webhosting machine
# this server will accept image and pass on to browser

import socket
import os, sys
from _thread import *
import json
import io
import fileinput


LINE_COUNT = 0
MAX_LINES = 10


ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1234 # uses this port to talk to raspberry pi # expose this port 
ThreadCount = 0
try:
    ServerSocket.bind(('', port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

print ('Initializing state file...')

state_path = os.getcwd() + "/state" # assuming that you call from saraiya-scope-v2 root directory
if os.path.exists(state_path) == False:
    print('Creating state file at...', state_path)
    f = open(state_path, "w+")
else:
    print('Using existing state file at...', state_path)

# handles the connection from the raspberry pi
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    max_lines = 10
    
    while True:
        data = connection.recv(2048)
        raw_data = data.decode('utf-8')
        print('received: ', raw_data)
        
        with open(state_path, 'w+') as file:
            contents = file.read()
            num_lines = len(contents.split("\n"))
            file.seek(0)
            if num_lines >= 10:
                file.seek(1) # delete everything except 1 line so it doesn't crash
                file.truncate()
                file.seek(0)
                file.write(raw_data+"\n")
            else:
                file.write(raw_data+"\n"+contents)
        
        if not data:
            break
        connection.sendall(str.encode(raw_data))
    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
# ServerSocket.close()
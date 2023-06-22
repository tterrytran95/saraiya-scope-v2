import time, sys, socket, json
from utils.sensor_utils import *

HOST = sys.argv[1].split("=")[1]
INT_TIME = sys.argv[2].split("=")[1]
PORT = 1234
TOTAL_FRAMES = 3080 # temp for now
SAMPLE_RATE = 1
THRESH = 15

## Step 1: Make socket connection to server ## 
ClientSocket = socket.socket()
print('Waiting for connection')
CONNECTED = False
while CONNECTED == False:
    try:
        print("Attempting to connect to {}:{}".format(HOST, PORT))
        print(ClientSocket.connect((HOST, PORT)))
        if ClientSocket.connect((HOST, PORT)) != None:
            CONNECTED = True
    except socket.error as e:
        print(str(e))
        exit(1)
    Response = ClientSocket.recv(1024)
    print("Server response: {}".format(Response))

## Step 2: Initialize sensors ## 
prox7, prox0, prox3, prox4 = initialize_sensors(INT_TIME)

## Step 3: Start sensors ## 
current = 'prox1'
previous = None
img_count = 0 # send this to host so they know which image to render
direction = None
current_sample = 0
state_count_dict = {}
stable_count = 0
while True:
    
    previous = current 
    
    prox_dict = {
        'p7' : prox7.proximity,
        'p0' : prox0.proximity,
        'p3' : prox3.proximity,
        'p4' : prox4.proximity,
    }
    
    print('######')
    print(prox_dict)


    if get_sensor(prox_dict) is not None:
        current = get_sensor(prox_dict)

        
    direction = get_direction(current, previous)

    if current_sample % SAMPLE_RATE == 0:
    
        direction = get_direction(current, previous)
        
        if direction == 'forward': 
            img_count = (img_count + 1) % TOTAL_FRAMES
            Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
            print("Forward response: {}".format(Response))
        elif direction == 'backward': 
            img_count = (img_count - 1) % TOTAL_FRAMES
            Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
            print("Backward response: {}".format(Response))
        else:
            stable_count += 1
            if stable_count >= 50:
                Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
                ClientSocket.send(str.encode(Input))
                Response = ClientSocket.recv(1024)
                print("Stable response: {}".format(Response))
                stable_count = 0 # reset it

    current_sample += 1
    time.sleep(.15)

ClientSocket.close()

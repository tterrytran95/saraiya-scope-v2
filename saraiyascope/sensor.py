# usage python3 sensor.py HOST=10.0.0.21

import time, sys, socket, json
from utils.sensor_utils import *

# HOST = '10.0.0.211' # ip address of displaying computer # terry's house
# HOST = '192.168.42.54' # ip address of displaying computer # alex's house 
# HOST = '192.168.1.26' # ip address of displaying computer # baltic mill


HOST = sys.argv[1].split("=")[1]
PORT = 1234
TOTAL_FRAMES = 3080 # temp for now
SAMPLE_RATE = 1
THRESH = 15

## Step 1: Make socket connection to server ## 
ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))
    exit(1)
Response = ClientSocket.recv(1024)

## Step 2: Initialize sensors ## 
prox7, prox0, prox3, prox4 = initialize_sensors()

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
    print(prox_dict)
    # current = get_trending_state(prox_dict)
    if get_sensor(prox_dict) is not None:
        current = get_sensor(prox_dict)
        # print("sensor triggered: ", current)
        
    direction = get_direction(current, previous, stable_count)
    print(direction)
    # state_count_dict = update_trend(state_count_dict, new_state)

    if current_sample % SAMPLE_RATE == 0:
    # if current != previous:
        # direction = get_trending_state(state_count_dict)
        direction = get_direction(current, previous)
        print("direction sent to server: ", direction)
        # print(state_count_dict)
        # state_count_dict = {} # reset this
        
        if direction == 'forward': 
            img_count = (img_count + 1) % TOTAL_FRAMES
            Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        elif direction == 'backward': 
            img_count = (img_count - 1) % TOTAL_FRAMES
            Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        else:
            Input = direction + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)

    current_sample += 1
    time.sleep(.15)


ClientSocket.close()
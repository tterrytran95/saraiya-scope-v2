# usage python3 sensor.py HOST=10.0.0.21

import time, sys, socket, json
from utils.sensor_utils import *

# HOST = '10.0.0.211' # ip address of displaying computer # terry's house
# HOST = '192.168.42.54' # ip address of displaying computer # alex's house 
# HOST = '192.168.1.26' # ip address of displaying computer # baltic mill


HOST = sys.argv[1].split("=")[1]
PORT = 1234
TOTAL_FRAMES = 3080 # temp for now
SAMPLE_RATE = 1000
THRESH = 30

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
prox1, prox2, prox3, prox4 = initialize_sensors()

## Step 3: Start sensors ## 
current = 'prox1'
previous = None
img_count = 0 # send this to host so they know which image to render
current_state = None
current_sample = 0
state_count_dict = {}
while True:
    
    previous = current 
    max_value = -1
    
    test_d = {
        # 'p1' : prox1.proximity_high_interrupt,
        # 'p2' : prox2.proximity_high_interrupt,
        # 'p3' : prox3.proximity_high_interrupt,
        # 'p4' : prox4.proximity_high_interrupt,
        'p1' : prox1.proximity,
        'p2' : prox2.proximity,
        'p3' : prox3.proximity,
        'p4' : prox4.proximity,
    }
    print(test_d)
    current = get_trending_state(test_d)
    print(current)
    new_state = get_state(current, previous)
    state_count_dict = update_trend(state_count_dict, new_state)

    if current_sample % SAMPLE_RATE == 0:
        current_state = get_trending_state(state_count_dict)
        print(current_state)
        print(state_count_dict)
        state_count_dict = {} # reset this
        
        if current_state == 'forward': 
            img_count = (img_count + 1) % TOTAL_FRAMES
            Input = current_state + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        elif current_state == 'backward': 
            img_count = (img_count - 1) % TOTAL_FRAMES
            Input = current_state + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        else:
            Input = current_state + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)

    current_sample += 1
    time.sleep(.15)


ClientSocket.close()
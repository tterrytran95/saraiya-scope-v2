import time
import board
import qwiic_tca9548a
import qwiic_proximity
import adafruit_tca9548a
import sys
import adafruit_vcnl4040
import socket
import json
# HOST = '10.0.0.211' # ip address of displaying computer
HOST = '192.168.42.54' # ip address of displaying computer
PORT = 1234
TOTAL_FRAMES = 3080 # temp for now



## determines the state of the sensors
def get_state(current, previous):
    # if current == previous:
    #     return 'stable'
    
    if current > previous:
        return 'forward'
    
    if current < previous:
        return 'backward'
    
def get_trending_state(count_dict):
    max_value = -1
    for k in count_dict:
        if count_dict[k] > max_value:
            state = k
            max_value = count_dict[k]
        return state

def update_trend(state_count_dict, new_state):
    if new_state in state_count_dict:
        state_count_dict[new_state] += 1
    else:
        state_count_dict[new_state] = 1
        
    for k in state_count_dict:
        if k != new_state:
            state_count_dict[k] = state_count_dict[k] - 1 if (state_count_dict[k] - 1 > 0) else 0
    return state_count_dict  


## make socket connection to serveru
ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((HOST, PORT))
except socket.error as e:
    print(str(e))
    exit(1)
Response = ClientSocket.recv(1024)

# Create I2C bus as normal
i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

prox1 = adafruit_vcnl4040.VCNL4040(tca[0])
# prox2 = adafruit_vcnl4040.VCNL4040(tca[7])
prox3 = adafruit_vcnl4040.VCNL4040(tca[4])
# prox4 = adafruit_vcnl4040.VCNL4040(tca[3])

current = 'prox1'
previous = None
img_count = 0 # send this to host so they know which image to render
cur_state = None
state_count_dict = {}
SAMPLE_RATE = 10
current_sample = 0
while True:
    
    previous = current 
    max_value = -1
    
    p1 = prox1.proximity
    if p1 > max_value:
        current = 'prox1'
        max_value = p1
    
    # p2 = prox2.proximity
    # if p2 > max_value:
    #     current = 'prox2'
    #     max_value = p2
    
    p3 = prox3.proximity
    if p3 > max_value:
        current = 'prox3'
        max_value = p3
        
    # p4 = prox4.proximity
    # if p4 > max_value:
    #     current = 'prox4'
    #     max_value = p4

    new_state = get_state(current, previous)
    state_count_dict = update_trend(state_count_dict, new_state)
    print(state_count_dict)
    
    # networking stuff 
    # if (cur_state == 'stable' and cur_state == get_state(current, previous)):
    #     cur_state = get_state(current,previous)
    #     pass # don't send it bc it's it's stable
    # else: # update the input 
    #     cur_state = get_state(current,previous)
    #     # cur_state = get_avg_state(state_count_dict)
    #     print("1", state_count_dict)
        
    #     if cur_state == 'forward': 
    #         img_count = (img_count + 1) % TOTAL_FRAMES
    #     elif cur_state == 'backward': 
    #         img_count -= 1
    #         if img_count < 0: img_count == 0
        
        
        # Input = cur_state + ',' + 'frame'+str(img_count*10)+'.jpg'
        # ClientSocket.send(str.encode(Input))
        # Response = ClientSocket.recv(1024)
        # print(Response.decode('utf-8'))
    
    if current_sample % SAMPLE_RATE == 0:
        cur_state = get_trending_state(state_count_dict)
        print(cur_state)
        print(state_count_dict)
        state_count_dict = {} # reset this
        
        if cur_state == 'forward': 
            img_count = (img_count + 1) % TOTAL_FRAMES
            Input = cur_state + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        elif cur_state == 'backward': 
            img_count -= 1
            if img_count < 0: img_count == 0
            Input = cur_state + ',' + 'frame'+str(img_count*10)+'.jpg'
            ClientSocket.send(str.encode(Input))
            Response = ClientSocket.recv(1024)
        
    current_sample += 1
    time.sleep(.10)


ClientSocket.close()
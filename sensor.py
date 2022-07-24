import time
import board
import qwiic_tca9548a
import qwiic_proximity
import adafruit_tca9548a
import sys
import adafruit_vcnl4040

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

    
def get_state(current, previous):
    if current == previous:
        return 'stable'
    
    if current > previous:
        return 'forward'
    
    if current < previous:
        return 'backward'

# Create I2C bus as normal
i2c = board.I2C()

# Create the TCA9548A object and give it the I2C bus
#tca = qwiic_tca9548a.QwiicTCA9548A()
tca = adafruit_tca9548a.TCA9548A(i2c)

prox1 = adafruit_vcnl4040.VCNL4040(tca[0])
prox2 = adafruit_vcnl4040.VCNL4040(tca[7])
prox3 = adafruit_vcnl4040.VCNL4040(tca[4])
prox4 = adafruit_vcnl4040.VCNL4040(tca[3])

current = 'prox1'
previous = None

while True:
    previous = current 
    max_value = -1
    
    p1 = prox1.proximity
    if p1 > max_value:
        current = 'prox1'
        max_value = p1
    
    p2 = prox2.proximity
    if p2 > max_value:
        current = 'prox2'
        max_value = p2
    
    p3 = prox3.proximity
    if p3 > max_value:
        current = 'prox3'
        max_value = p3
        
    p4 = prox4.proximity
    if p4 > max_value:
        current = 'prox4'
        max_value = p4
    
    print(get_state(current, previous))
    
    # Input = input('Say Something: ')
    Input = get_state(current, previous)
    # ClientSocket.sendall(str.encode(Input))
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

          
    time.sleep(.25)
ClientSocket.close()
import qwiic_tca9548a
import qwiic_proximity
import adafruit_tca9548a
import adafruit_vcnl4040
import board
import sys

THRESH = 15
# INT_TIME = sys.argv[1].split("=")[1]

# utils for sensor
def initialize_sensors(INT_TIME):
    # Create I2C bus as normal
    i2c = board.I2C()

    # Create the TCA9548A object and give it the I2C bus
    tca = adafruit_tca9548a.TCA9548A(i2c)

    prox7 = adafruit_vcnl4040.VCNL4040(tca[7])
    prox0 = adafruit_vcnl4040.VCNL4040(tca[0])
    prox3 = adafruit_vcnl4040.VCNL4040(tca[3])
    prox4 = adafruit_vcnl4040.VCNL4040(tca[4])
    
    if INT_TIME == '2.5':
        prox7.proximity_integration_time=prox7.PS_2_5T
        prox0.proximity_integration_time=prox0.PS_2_5T
        prox3.proximity_integration_time=prox3.PS_2_5T
        prox4.proximity_integration_time=prox4.PS_2_5T
    elif INT_TIME == '3.0':
        prox7.proximity_integration_time=prox7.PS_3T
        prox0.proximity_integration_time=prox0.PS_3T
        prox3.proximity_integration_time=prox3.PS_3T
        prox4.proximity_integration_time=prox4.PS_3T
    elif INT_TIME == '3.5':
        prox7.proximity_integration_time=prox7.PS_3_5T
        prox0.proximity_integration_time=prox0.PS_3_5T
        prox3.proximity_integration_time=prox3.PS_3_5T
        prox4.proximity_integration_time=prox4.PS_3_5T
    elif INT_TIME == '4.0':
        prox7.proximity_integration_time=prox7.PS_4T
        prox0.proximity_integration_time=prox0.PS_4T
        prox3.proximity_integration_time=prox3.PS_4T
        prox4.proximity_integration_time=prox4.PS_4T
    elif INT_TIME == '8.0':
        prox7.proximity_integration_time=prox7.PS_8T
        prox0.proximity_integration_time=prox0.PS_8T
        prox3.proximity_integration_time=prox3.PS_8T
        prox4.proximity_integration_time=prox4.PS_8T

    return prox7, prox0, prox3, prox4


def get_sensor(prox_dict):
    for k in prox_dict:
        if prox_dict[k] >= THRESH: 
            return k
    return None        


def is_forward(current, previous):
    if (current == 'p7' and previous == 'p3') or (current == 'p3' and previous == 'p6') \
        or (current == 'p6' and previous == 'p4') or (current == 'p4' and previous == 'p7'):
            return True
        
def is_backward(current, previous):
    if (current == 'p3' and previous == 'p7') or (current == 'p7' and previous == 'p4') \
        or (current == 'p4' and previous == 'p6') or (current == 'p6' and previous == 'p3'):
            return True

## determines the state of the sensors
def get_direction(current, previous):
    if is_forward(current, previous): return 'forward'
    elif is_backward(current, previous): return 'backward'
    else: return 'stable'
    
def get_trending_state(count_dict):
    max_value = -1
    state = 'stable'
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

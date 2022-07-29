import qwiic_tca9548a
import qwiic_proximity
import adafruit_tca9548a
import adafruit_vcnl4040
import board

# utils for sensor
def initialize_sensors():
    # Create I2C bus as normal
    i2c = board.I2C()

    # Create the TCA9548A object and give it the I2C bus
    tca = adafruit_tca9548a.TCA9548A(i2c)

    prox1 = adafruit_vcnl4040.VCNL4040(tca[7])
    prox2 = adafruit_vcnl4040.VCNL4040(tca[0])
    prox3 = adafruit_vcnl4040.VCNL4040(tca[3])
    prox4 = adafruit_vcnl4040.VCNL4040(tca[4])

    prox1.proximity_high_threshold=20
    prox2.proximity_high_threshold=20
    prox3.proximity_high_threshold=20
    prox4.proximity_high_threshold=20

    prox1.proximity_interrupt=prox1.PS_INT_CLOSE
    prox2.proximity_interrupt=prox2.PS_INT_CLOSE
    prox3.proximity_interrupt=prox3.PS_INT_CLOSE
    prox4.proximity_interrupt=prox4.PS_INT_CLOSE
    
    return prox1, prox2, prox3, prox4


def get_sensor(prox_dict):
    for k in prox_dict:
        if prox_dict[k] == True: 
            return k
    return None        


## determines the state of the sensors
def get_direction(current, previous):
    if current == previous:
        return 'stable'
    
    if current > previous:
        return 'forward'
    
    if current < previous:
        return 'backward'
    
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

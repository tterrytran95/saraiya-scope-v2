# saraiya-scope-v2

# how to run 
- Pull of 3 terminal windws
- Window 1: Rapsberry pi 
    - ```ssh saraiya-scope@raspberrypi``` 
    - Enter password set by IT 
- Window 2: 


### System requirements
- Iot device (raspberry pi) must be connected to the same Wifi network as the displaying laptop. 

### Set up the raspberry pi
1. Ssh into the raspberry pi. [Instructions](https://libguides.nyit.edu/c.php?g=469894&p=3365470)
    - ```ssh saraiya-scope@[IP_ADDRESS]```
- Find IP_ADDRESS by running ```ifconfig``` on the raspberry pi terminal on initial boot. This requires a monitor, keyboard, and mouse for the pi. 
- Clone this directory: 

### Set up the local machine 
- This node is responsible for receiving the stream of data from the IoT device (the raspberry pi)
1. Get the ip address of this node. [Instructions](https://www.hellotech.com/guide/for/how-to-find-ip-address-on-mac)
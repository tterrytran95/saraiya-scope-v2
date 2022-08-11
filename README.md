# saraiya-scope-v2

### system requirements
- Iot device (raspberry pi) must be connected to the same Wifi network as the displaying laptop. 

# how to run 
- Open 3 command line windows 

- Window 1: Front end server
    - ```cd saraiya-scope-v2```
    - ```python3 manage.py runserver```
    - This should start the webserver. You can open up a web browser and check [this link](http://localhost:8000/museum_image?img=frame0.jpg)

- Window 2: Backend server 
    - ```cd saraiya-scope-v2/saraiyascope```
    - ```python3 server.py```

- Window 3: Rapsberry pi 
    - ```ssh saraiya-scope@raspberrypi``` 
    - Enter password set by IT 
    - ```cd saraiya-scope-v2/saraiyascope```
    - ```python3 sensor.py HOSTNAME=192.168.1.26 INT_TIME=4.0```
    - Options for ```INT_TIME``` are as follows: 2.5, 3.0, 3.5, 4.0, 8.0
    - ```INT_TIME``` is a flag that you can use to tune the time between sampling data points 
    - The larger the ```INT_TIME```, the longer the delay between two data points. 

- Open up a webrowser on the laptop
    - Put this into the url: http://localhost:8000/museum_image?img=frame0.jpg
    - Refresh the page after starting both servers 

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
    - ```python3 sensor.py```

- Open up a webrowser
    - Put this into the url: http://localhost:8000/museum_image?img=frame0.jpg
    - Refresh the page after starting both servers 

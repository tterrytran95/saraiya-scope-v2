# saraiya-scope-v2

## System requirements
- Iot device (raspberry pi) must be connected to the same Wifi network as the displaying laptop. 

## How to install 
Please have these ready before starting the software installation process:
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [python3 version 3.9.6](https://www.python.org/downloads/)
- Someway to clone the repository
    - Option 1: Provide an ssh-key to tterrytran95@gmail.com 
        - ssh public key id of host machine 
        - Get the public key by running ```ssh-keygen``` on the command line
        - Find it with ```cd .ssh && cat id_rsa.pub```
        - Send this to tterrytran95@gmail.com 
    - Option 2: Fork off 
        - Assuming the user has a github account already, please fork off the original repo
        - No sharing of public key required 

1. ```git clone git@github.com:tterrytran95/saraiya-scope-v2.git```
2. ```pip3 install requests opencv-python```
3. ```cd saraiya-scope-v2/saraiyascope && mkdir samples && mkdir frames && touch state```
4. Drop video file titled mochu_ks.mp4 into the saraiyascope saraiya-scope-v2/saraiyascope/samples directory
5. ```cd utils```
6. ```python3 image_utils.py```
    - This will create the frames and upload them to the django server 
    - It will take a minute
7. ```cd ../```
    - Go back into the directory saraiyascope 
8. ```python3 makemigrations```
9. ```python3 migrate```
    - This is the last step. Within steps 6-9, we are basically splitting the images and putting them on the local database to be consumed by the frontend server. 

# How to run 
- Open 3 command line windows 

- Window 1: Front end server
    1. ```cd saraiya-scope-v2```
    2. ```python3 manage.py runserver```
    3. This should start the webserver. You can open up a web browser and check [this link](http://localhost:8000/museum_image?img=frame0.jpg)

- Window 2: Backend server 
    1. ```cd saraiya-scope-v2/saraiyascope```
    2. ```python3 server.py```

- Window 3: Rapsberry pi 
    1. ```ssh saraiya-scope@raspberrypi``` 
        - Enter password set by IT 
    2. ```cd saraiya-scope-v2/saraiyascope```
    3. ```python3 sensor.py HOSTNAME=192.168.1.26 INT_TIME=3.5```
        - ```HOSTNAME``` is the listening IP address of the laptop. 
        - Options for ```INT_TIME``` are as follows: 2.5, 3.0, 3.5, 4.0, 8.0
        - ```INT_TIME``` is a flag that you can use to tune the time between sampling data points 
        - The larger the ```INT_TIME```, the longer the delay between two data points. 

- Open up a webrowser on the laptop
    - Put this into the url: http://localhost:8000/museum_image?img=frame0.jpg
    - Refresh the page after starting both servers 

# saraiya-scope-v2

## System prerequisites
- Linux OS distribution
- Iot device (raspberry pi) must be connected to the same Wifi network as the displaying laptop (used interchangeably as the frontend/backend server). 
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on the front/backend server 
- [python3 version 3.9.6](https://www.python.org/downloads/) on the front/backend server
- Someway to clone the repository
    - Option 1: Provide an ssh-key to tterrytran95@gmail.com 
        - ssh public key id of host machine 
        - Get the public key by running ```ssh-keygen``` on the command line
        - Find it with ```cd .ssh && cat id_rsa.pub```
        - Send this to tterrytran95@gmail.com 
    - Option 2: Fork off 
        - Assuming the user has a github account already, please fork off the original repo
        - No sharing of public key required 

## How to install on displaying computer 
1. ```git clone git@github.com:tterrytran95/saraiya-scope-v2.git``` 
    - Or this will be your own forked repository
2. ```pip3 install -U Django requests opencv-python channels Pillow```
3. ```cd saraiya-scope-v2/ && touch state```
4. Open up another command line terminal and run ```python3 manage.py runserver```
    - Leave this alone and return back to the other terminal to run steps 5-6
    - Should be in the ```saraiya-scope-v2``` directory where ```manage.py``` lives
5. ```python3 manage.py makemigrations```
6. ```python3 manage.py migrate```
7. ```cd saraiyascope && mkdir samples && mkdir frames```
8. Drop video file titled ```mochu_ks.mp4``` into the directory ```saraiya-scope-v2/saraiyascope/samples```
9. ```cd utils```
10. ```python3 image_utils.py```
    - This will create the frames and upload them to the django server 
    - It will take a minute
Done! 

## How to run 
1. Open 3 command line windows 
2. Window 1: Front end server
    - ```cd saraiya-scope-v2```
    - ```python3 manage.py runserver```
    - This should start the webserver. You can open up a web browser and check [this link](http://localhost:8000/museum_image?img=frame0.jpg)
3. Window 2: Backend server 
    - ```cd saraiya-scope-v2/saraiyascope```
    - ```python3 server.py```
    - ```python3 saraiyascope/test-socket.py HOST=127.0.0.1``` for test environments
4. Window 3: Rapsberry pi 
    - ```ssh saraiya-scope@raspberrypi``` 
        - Enter password set by IT 
    - ```cd saraiya-scope-v2/saraiyascope```
    - ```git pull``` 
    - ```python3 sensor.py HOSTNAME=192.168.1.26 INT_TIME=3.5```
        - ```HOSTNAME``` is the listening IP address of the laptop. 
        - Options for ```INT_TIME``` are as follows: 2.5, 3.0, 3.5, 4.0, 8.0
        - ```INT_TIME``` is a flag that you can use to tune the time between sampling data points 
        - The larger the ```INT_TIME```, the longer the delay between two data points. 
5. Open up a webrowser on the laptop
    - Put this into the url: http://localhost:8000/museum_image?img=frame0.jpg
    - Refresh the page after starting both servers 

### NEW SETUP

### Initializations
1. Get the code with the sample embedded into it 
2. Set up the terminal environment (just use 2)
3. Terminal 1 - cd saraiya
    source initialize.sh


source server.sh
python3 saraiyascope/sensor.py HOST=10.0.0.16 INT_TIME=4.0
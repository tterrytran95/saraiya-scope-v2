import json
import time, os
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
STATE = os.getcwd() + "/state" # path on baltic mill
print("current working directory: ", os.getcwd())
print(STATE)

# single threaded 
# museum consumer for django channel
class MuseumConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        prefix="http://127.0.0.1:8000/media/images/" # talk with the front end # hit the end media/images/ end point to display 
        
        while True:
            try:
                with open(STATE, 'r') as file:
                    file.seek(0)
                    line = file.readline()
                    
                    if line == "":
                        continue
                    else:
                        line_contents = line.split(",")
                        if len(line_contents) < 2:
                            continue
                        else:
                            img = line_contents[1]
                            res = self.send(json.dumps({'img':prefix+img}))
                    print(img)
            except Exception as e:
                print(e)

    def receive(self):
        pass


import json
import time
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
STATE = os.getcwd() + "/state" # path on baltic mill

# museum consumer for django channel
class MuseumConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        prefix="http://localhost:8000/media/images/"
        
        while True:
            with open(STATE, 'r') as file:
                file.seek(0)
                line = file.readline()
                print('LINE', line)
                
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
                    
    def receive(self):
        pass


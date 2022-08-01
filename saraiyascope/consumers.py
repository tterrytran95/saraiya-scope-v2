import json
import time
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
# STATE = "/Users/tuethutran/saraiya-scope-venv/saraiya-scope-v2/saraiyascope/state" # path on baltic mill
STATE = "C:/Users/admin/projects/saraiya-scope-v2/saraiyascope/state" # path on baltic mill

# museum consumer for django channel
class MuseumConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        prefix="http://localhost:8000/media/images/"
        
        # for i in range(1000, 3000):
        MAX_FRAMES = 3000
        # i = 0
        # while true:
        #     cur_frame = (i * 10) % MAX_FRAMES
        #     img = 'frame'+str(cur_frame)+'.jpg'
        #     res = self.send(json.dumps({'img':prefix+img}))
        #     print('response:', res)
        #     time.sleep(.10)
            
        # await self.close()
        while True:
            with open(STATE, 'r') as file:
                file.seek(0)
                line = file.readline().split(",")
                if len(line) < 2:
                    continue
                else:
                    img=line[1]
                res = self.send(json.dumps({'img':prefix+img}))
                print(img)
                    
    def receive(self):
        pass


import json
import time
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# museum consumer for django channel
class MuseumConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        prefix="http://localhost:8000/media/images/"
        
        for i in range(1000, 3000):
            img = 'frame'+str(i*10)+'.jpg'
            res = self.send(json.dumps({'img':prefix+img}))
            print('response:', res)
            time.sleep(.10)
            
        # await self.close()
        
        # while True:
        #     with open('/Users/tuethutran/saraiya-scope-venv/saraiya-scope-v2/saraiyascope/state', 'r') as file:
        #         file.seek(0)
        #         img=file.readline().split(",")[1]
        #         res = self.send(json.dumps({'img':prefix+img}))
        #         print(img)
    
    def receive(self):
        pass


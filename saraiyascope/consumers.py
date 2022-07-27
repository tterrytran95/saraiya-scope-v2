import json
import time
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

# museum consumer for django channel
class MuseumConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        prefix="http://localhost:8000/media/images/"
        for i in range(0, 3000):
            img = 'frame'+str(i*10)+'.jpg'
            res = self.send(json.dumps({'img':prefix+img}))
            print('response:', res)
            time.sleep(.10)
        # await self.close()
    
    def receive(self):
        pass

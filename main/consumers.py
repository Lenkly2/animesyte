import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

ROOMS_STATE = {}

class PlayerConsumer(WebsocketConsumer):
    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'room_{self.room_id}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

        state = ROOMS_STATE.get(self.room_id, {"paused":False,"time":0,"episode":1})
        self.send(text_data=json.dumps({
            "type":"sync",
            **state
        }))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
    
    def receive(self, text_data):
        data = json.loads(text_data)
        current = ROOMS_STATE.get(self.room_id, {"paused":False,"time":0,"episode":1})

        if "paused" in data:
            current["paused"] = data["paused"]
        if "time" in data:
            current["time"] = data["time"]
        if "episode" in data:
            current["episode"] = data["episode"]

        ROOMS_STATE[self.room_id]= current

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {   
                "type": "player_update",
                "paused": current["paused"],
                "time": current["time"],
                "episode": current["episode"],
            }
        )

        # self.send(text_data=json.dumps({
        #     "type":"sync",
        #     "paused":data['paused'],
        #     "time":data["time"],
        # }))
    def player_update(self,event):
        self.send(text_data=json.dumps({
            "type":"sync",
            "paused":event['paused'],
            "time":event["time"],
            "episode":event["episode"],
        }))
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
from django.conf import settings

from app.models import History



class EchoConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        print("Recevied!")
        message = event["text"]
        # message = transcriber(message)[0]["translation_text"]
        await self.send({
            "type": "websocket.send",
            "text": message,
        })
        print("Replied")
        
    async def websocket_disconnect(self, event):
        print('Disconnected', event)
        await self.send({
            "type": "websocket.disconnect",
        })
        await self.disconnect(event["code"])
        raise StopConsumer()
        
    async def disconnect(self, code):
        """
        Called when a WebSocket connection is closed.
        """
        pass
        
        

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        
        

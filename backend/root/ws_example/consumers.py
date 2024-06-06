import asyncio
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class WsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("robots", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("robots", self.channel_name)

    async def send_update(self, event):
        await self.send(text_data=json.dumps({"message": event['message']}))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.send(text_data=json.dumps({"message": message}))
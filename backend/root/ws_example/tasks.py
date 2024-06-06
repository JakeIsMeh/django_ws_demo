from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

counter = 0

async def send_to_channel():
    global counter # never use global this is just a hack for the demo
    channel_layer = get_channel_layer()
    await channel_layer.group_send("robots", { 'type': 'send_update', "message": str(counter), })
    counter += 1

@shared_task
def trigger_send_to_channel():
    async_to_sync(send_to_channel)()

from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/", consumers.WsConsumer.as_asgi()),
]

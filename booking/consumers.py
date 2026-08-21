import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificacionConsumer(AsyncWebsocketConsumer):

    async def connect(self ):

         id_profesional = self.scope['url_route']['kwargs']['id_profesional']

         self.nombre_grupo = f"profesional_{id_profesional}"

         await self.channel_layer.group_add(self.nombre_grupo, self.channel_name)
         await self.accept()
         
    async def disconnect(self, close_code):

         await self.channel_layer.group_discard(self.nombre_grupo, self.channel_name)

    async def enviar_notificaciones(self, event):

         mensaje =event['contenido']
         await self.send(text_data=json.dumps(mensaje))
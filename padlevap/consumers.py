import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

# Don't import models at the top level - use get_user_model() and import inside functions

class ChatConsumer(AsyncWebsocketConsumer):
   

    async def connect(self):
        # Debug: Print headers to see what's coming in
        headers = dict(self.scope.get('headers', {}))
        print("Headers received:", headers)
        
        # Temporary: Accept all connections for testing
        await self.accept()
        
        # Try to get user from scope
        user = self.scope.get('user')
        if user and not user.is_anonymous:
            self.user = user
            self.user_group_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(
                self.user_group_name,
                self.channel_name
            )
            print(f"User {self.user.id} connected")
        else:
            print("Anonymous user connected")    

    async def disconnect(self, close_code):
        # Leave user group
        if hasattr(self, 'user_group_name'):
            await self.channel_layer.group_discard(
                self.user_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_type = data.get('type')
            
            if message_type == 'send_message':
                await self.handle_send_message(data)
            elif message_type == 'mark_read':
                await self.handle_mark_read(data)
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def handle_send_message(self, data):
        receiver_id = data.get('receiver_id')
        content = data.get('content')
        
        if not receiver_id or not content:
            return

        # Save message to database
        message = await self.save_message(self.user.id, receiver_id, content)
        
        if message:
            # Serialize message
            message_data = await self.serialize_message(message)
            
            # Send to receiver
            receiver_group = f"user_{receiver_id}"
            await self.channel_layer.group_send(
                receiver_group,
                {
                    'type': 'new_message',
                    'message': message_data
                }
            )
            
            # Send confirmation to sender
            await self.send(text_data=json.dumps({
                'type': 'message_sent',
                'message': message_data
            }))

    async def handle_mark_read(self, data):
        message_id = data.get('message_id')
        if message_id:
            await self.mark_message_read(message_id, self.user.id)

    async def new_message(self, event):
        """Handle new message from channel layer"""
        await self.send(text_data=json.dumps({
            'type': 'new_message',
            'message': event['message']
        }))

    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, content):
        from .models import Message  # Import inside the function
        User = get_user_model()
        try:
            sender = User.objects.get(id=sender_id)
            receiver = User.objects.get(id=receiver_id)
            message = Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content
            )
            return message
        except User.DoesNotExist:
            return None

    @database_sync_to_async
    def serialize_message(self, message):
        from .serializers import MessageSerializer  # Import inside the function
        serializer = MessageSerializer(message)
        return serializer.data

    @database_sync_to_async
    def mark_message_read(self, message_id, user_id):
        from .models import Message  # Import inside the function
        try:
            Message.objects.filter(
                id=message_id, 
                receiver_id=user_id
            ).update(is_read=True)
        except:
            pass
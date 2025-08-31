# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
# DO NOT import User model at module level - it causes AppRegistryNotReady error

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        if self.user.is_anonymous:
            await self.close()
            return

        # Create a unique group name for this user
        self.user_group_name = f"user_{self.user.id}"
        
        # Join user group
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )
        
        await self.accept()
        print(f"User {self.user.id} connected to chat")

    async def disconnect(self, close_code):
        # Leave user group
        if hasattr(self, 'user_group_name'):
            await self.channel_layer.group_discard(
                self.user_group_name,
                self.channel_name
            )
        
        if hasattr(self, 'user'):
            print(f"User {self.user.id} disconnected from chat")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_type = data.get('type')
            
            if message_type == 'send_message':
                await self.handle_send_message(data)
            elif message_type == 'mark_read':
                await self.handle_mark_read(data)
            elif message_type == 'typing':
                await self.handle_typing(data)
            elif message_type == 'stopped_typing':
                await self.handle_stopped_typing(data)
        except Exception as e:
            print(f"Error handling message: {str(e)}")
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def handle_send_message(self, data):
        receiver_id = data.get('receiver_id')
        content = data.get('content')
        
        if not receiver_id or not content:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Missing receiver_id or content'
            }))
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
            
            print(f"Message sent from user {self.user.id} to user {receiver_id}")

    async def handle_mark_read(self, data):
        message_id = data.get('message_id')
        if message_id:
            await self.mark_message_read(message_id, self.user.id)

    async def handle_typing(self, data):
        receiver_id = data.get('receiver_id')
        if receiver_id:
            receiver_group = f"user_{receiver_id}"
            await self.channel_layer.group_send(
                receiver_group,
                {
                    'type': 'user_typing',
                    'user_id': self.user.id
                }
            )

    async def handle_stopped_typing(self, data):
        receiver_id = data.get('receiver_id')
        if receiver_id:
            receiver_group = f"user_{receiver_id}"
            await self.channel_layer.group_send(
                receiver_group,
                {
                    'type': 'user_stopped_typing',
                    'user_id': self.user.id
                }
            )

    # Channel layer message handlers
    async def new_message(self, event):
        """Handle new message from channel layer"""
        await self.send(text_data=json.dumps({
            'type': 'new_message',
            'message': event['message']
        }))

    async def user_typing(self, event):
        """Handle typing notification"""
        await self.send(text_data=json.dumps({
            'type': 'user_typing',
            'user_id': event['user_id']
        }))

    async def user_stopped_typing(self, event):
        """Handle stopped typing notification"""
        await self.send(text_data=json.dumps({
            'type': 'user_stopped_typing',
            'user_id': event['user_id']
        }))

    # Database operations - Import models inside functions to avoid AppRegistryNotReady
    @database_sync_to_async
    def save_message(self, sender_id, receiver_id, content):
        from .models import Message  # Import inside function
        User = get_user_model()      # Get custom user model
        
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
            print(f"User not found: sender={sender_id}, receiver={receiver_id}")
            return None
        except Exception as e:
            print(f"Error saving message: {str(e)}")
            return None

    @database_sync_to_async
    def serialize_message(self, message):
        from .serializers import MessageSerializer  # Import inside function
        serializer = MessageSerializer(message)
        return serializer.data

    @database_sync_to_async
    def mark_message_read(self, message_id, user_id):
        from .models import Message  # Import inside function
        
        try:
            Message.objects.filter(
                id=message_id, 
                receiver_id=user_id
            ).update(is_read=True)
            print(f"Message {message_id} marked as read by user {user_id}")
        except Exception as e:
            print(f"Error marking message as read: {str(e)}")

# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Message, ChatRoom, OnlineUser
from .serializers import MessageSerializer

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']
        
        # Check if user is authenticated
        if not self.user.is_authenticated:
            await self.close()
            return
        
        # Check if user is member of the room
        is_member = await self.check_room_membership()
        if not is_member:
            await self.close()
            return
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Mark user as online
        await self.mark_user_online()
        
        # Notify others that user joined
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_status',
                'action': 'joined',
                'user_data': await self.get_user_data()
            }
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            # Mark user as offline
            await self.mark_user_offline()
            
            # Notify others that user left
            if self.user.is_authenticated:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'user_status',
                        'action': 'left',
                        'user_data': await self.get_user_data()
                    }
                )
            
            # Leave room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get('type', 'message')
            
            if message_type == 'message':
                await self.handle_message(text_data_json)
            elif message_type == 'typing':
                await self.handle_typing(text_data_json)
            elif message_type == 'read_receipt':
                await self.handle_read_receipt(text_data_json)
            elif message_type == 'heartbeat':
                await self.handle_heartbeat()
                
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON format'
            }))
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))

    async def handle_message(self, data):
        """Handle incoming chat message"""
        message_content = data.get('message', '')
        parent_message_id = data.get('parent_message_id')
        message_type = data.get('message_type', 'text')
        
        if not message_content.strip():
            return
        
        # Save message and get serialized data
        message_data = await self.save_and_serialize_message(
            message_content,
            parent_message_id,
            message_type
        )
        
        if message_data:
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message_data': message_data
                }
            )

    async def handle_typing(self, data):
        """Handle typing indicator"""
        is_typing = data.get('is_typing', False)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'typing_indicator',
                'user_data': await self.get_user_data(),
                'is_typing': is_typing
            }
        )

    async def handle_read_receipt(self, data):
        """Handle read receipt"""
        message_id = data.get('message_id')
        if message_id:
            await self.mark_message_read(message_id)

    async def handle_heartbeat(self):
        """Handle heartbeat to keep user online"""
        await self.mark_user_online()
        await self.send(text_data=json.dumps({
            'type': 'heartbeat_ack'
        }))

    # WebSocket event handlers
    async def chat_message(self, event):
        """Send chat message to WebSocket"""
        await self.send(text_data=json.dumps({
            'type': 'message',
            'data': event['message_data']
        }))

    async def typing_indicator(self, event):
        """Send typing indicator to WebSocket"""
        # Don't send typing indicator back to the sender
        if event['user_data']['id'] != self.user.id:
            await self.send(text_data=json.dumps({
                'type': 'typing',
                'user': event['user_data'],
                'is_typing': event['is_typing']
            }))

    async def user_status(self, event):
        """Send user status change to WebSocket"""
        # Don't send status back to the sender
        if event['user_data']['id'] != self.user.id:
            await self.send(text_data=json.dumps({
                'type': 'user_status',
                'action': event['action'],
                'user': event['user_data']
            }))

    # Database operations
    @database_sync_to_async
    def mark_user_online(self):
        """Mark user as online in the room"""
        try:
            room = ChatRoom.objects.get(name=self.room_name)
            online_user, created = OnlineUser.objects.get_or_create(
                user=self.user,
                room=room
            )
            online_user.save()  # Updates last_seen
        except ChatRoom.DoesNotExist:
            pass

    @database_sync_to_async
    def mark_user_offline(self):
        """Remove user from online users"""
        try:
            room = ChatRoom.objects.get(name=self.room_name)
            OnlineUser.objects.filter(user=self.user, room=room).delete()
        except ChatRoom.DoesNotExist:
            pass

    @database_sync_to_async
    def mark_message_read(self, message_id):
        """Mark message as read by current user"""
        try:
            message = Message.objects.get(id=message_id)
            message.read_by.add(self.user)
        except Message.DoesNotExist:
            pass_to_async
    def check_room_membership(self):
        """Check if user is member of the room"""
        try:
            room = ChatRoom.objects.get(name=self.room_name, is_active=True)
            return room.members.filter(id=self.user.id).exists()
        except ChatRoom.DoesNotExist:
            return False

    @database_sync_to_async
    def get_user_data(self):
        """Get serialized user data"""
        from .serializers import UserSerializer
        serializer = UserSerializer(self.user)
        return serializer.data

    @database_sync_to_async
    def save_and_serialize_message(self, content, parent_message_id=None, message_type='text'):
        """Save message and return serialized data"""
        try:
            room = ChatRoom.objects.get(name=self.room_name)
            
            parent_message = None
            if parent_message_id:
                try:
                    parent_message = Message.objects.get(
                        id=parent_message_id,
                        room=room
                    )
                except Message.DoesNotExist:
                    pass
            
            # Create message
            message = Message.objects.create(
                room=room,
                user=self.user,
                content=content,
                message_type=message_type,
                parent_message=parent_message
            )
            
            # Serialize the message
            serializer = MessageSerializer(message)
            return serializer.data
            
        except ChatRoom.DoesNotExist:
            return {'error': 'Room not found'}
        except Exception as e:
            return {'error': str(e)}



 
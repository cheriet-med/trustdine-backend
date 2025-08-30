# chat/jwt_middleware.py
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Import inside the method to avoid circular imports
        from django.contrib.auth.models import AnonymousUser
        from rest_framework_simplejwt.authentication import JWTAuthentication
        
        scope['user'] = AnonymousUser()
        
        # Get headers from scope
        headers = dict(scope.get('headers', []))
        
        # Check for authorization header
        if b'authorization' in headers:
            try:
                auth_header = headers[b'authorization'].decode()
                
                # Extract token (support both JWT and Bearer prefixes)
                if auth_header.startswith('JWT '):
                    token = auth_header[4:]
                elif auth_header.startswith('Bearer '):
                    token = auth_header[7:]
                else:
                    token = auth_header  # Try without prefix
                
                # Validate JWT token
                if token:
                    jwt_auth = JWTAuthentication()
                    validated_token = jwt_auth.get_validated_token(token)
                    scope['user'] = await self.get_user(validated_token)
                    
            except Exception as e:
                print(f"JWT authentication failed: {e}")
                scope['user'] = AnonymousUser()
        
        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def get_user(self, validated_token):
        from django.contrib.auth import get_user_model
        from django.contrib.auth.models import AnonymousUser
        from rest_framework_simplejwt.authentication import JWTAuthentication
        
        try:
            user = JWTAuthentication().get_user(validated_token)
            return user
        except:
            return AnonymousUser()
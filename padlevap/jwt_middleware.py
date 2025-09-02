# chat/jwt_middleware.py
from urllib.parse import parse_qs
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Lazy import to avoid AppRegistryNotReady
        from django.contrib.auth.models import AnonymousUser
        from rest_framework_simplejwt.authentication import JWTAuthentication

        scope["user"] = AnonymousUser()
        token = None

        # --- 1) Check query string for ?token=xxx ---
        query_string = scope.get("query_string", b"").decode()
        if query_string:
            qs = parse_qs(query_string)
            if "token" in qs:
                token = qs["token"][0]

        # --- 2) Check Authorization header ---
        if not token:
            headers = dict(scope.get("headers", []))
            if b"authorization" in headers:
                auth_header = headers[b"authorization"].decode()
                if auth_header.startswith("JWT "):
                    token = auth_header[4:]
                elif auth_header.startswith("Bearer "):
                    token = auth_header[7:]
                else:
                    token = auth_header

        # --- 3) Validate JWT ---
        if token:
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(token)
                scope["user"] = await self.get_user(validated_token)
            except Exception as e:
                print(f"⚠️ JWT authentication failed: {e}")
                scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def get_user(self, validated_token):
        # Lazy import again
        from django.contrib.auth.models import AnonymousUser
        from rest_framework_simplejwt.authentication import JWTAuthentication

        try:
            return JWTAuthentication().get_user(validated_token)
        except Exception:
            return AnonymousUser()

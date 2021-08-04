import jwt
from django.conf import settings
from rest_framework import authentication
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            http_auth = request.META.get("HTTP_AUTHORIZATION")
            if http_auth is None:
                return None
            xjwt, token = http_auth.split(" ")
            decoded = jwt.decode(token, key=settings.SECRET_KEY, algorithms="HS256")
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, jwt.exceptions.DecodeError):
            return None

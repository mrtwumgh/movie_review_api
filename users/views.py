from rest_framework import generics
from users.serializers import (
    UserSerializer,
    RegistrationSerializer,
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': response.data,
            'token': token.key
        })




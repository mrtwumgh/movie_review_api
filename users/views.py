from rest_framework import generics, permissions
from users.serializers import (
    UserSerializer,
    RegistrationSerializer,
)
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from reviews.permissions import IsOwnerOrReadOnly



class UserRegistrationView(generics.CreateAPIView):
    """
    handles user registration, creating a user and returning a token.
    """
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



class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    retrieves or updates a user's profile, requiring authentication and ownership for updates.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user
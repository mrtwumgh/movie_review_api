from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from users.models import UserProfile
from reviews.models import Review
from reviews.serializers import ReviewSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Profile Model
    """
    class Meta:
        model = UserProfile
        fields = ['image', 'bio']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the  User Model
    """
    profile = UserProfileSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'reviews']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        bio = profile_data.get('bio')

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile = instance.profile
        if bio is not None:
            profile.bio = bio
            profile.save()

        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Registration
    """
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True, label="confirm password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user
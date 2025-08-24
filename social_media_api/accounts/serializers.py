from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        # Create token
        Token.objects.create(user=user)
        return user


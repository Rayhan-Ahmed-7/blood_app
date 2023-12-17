from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "phone_number"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["email", "password", "phone_number"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            self.instance = get_user_model().objects.get(email=email)
            # Authentication successful
            return data
        except get_user_model().DoesNotExist:
            # User does not exist
            msg = "Unable to log in with provided credentials."
            raise serializers.ValidationError(msg, code="authorization")
      

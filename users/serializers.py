from rest_framework import serializers
from django.contrib.auth.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long.")
        return value

    def validate_password(self, value):
        if len(value) < 8 or not re.search(r'\d', value):
            raise serializers.ValidationError("Password must be at least 8 characters and include a number.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

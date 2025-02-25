from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'role': {'read_only': True}}  # ensures that the role field is read-only

    def create(self, validated_data) -> User:
        password = validated_data.pop('password')
        user: User = User(**validated_data)
        user.set_password(password)  # This hashes the password
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)
        token['role'] = user.role
        return token

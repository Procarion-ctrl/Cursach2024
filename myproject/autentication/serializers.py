from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        con_password = validated_data.pop('confirm_password')
        if password != con_password:
            serializers.ValidationError('Підтвердження паролю не співпадає з ним.')
        user = User(username=username, email=email)
        user.password = make_password(password)
        user.save()
        return user
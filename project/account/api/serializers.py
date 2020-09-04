from rest_framework import serializers

from ..models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import request


# region register user api

class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password', 'password2', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'a user with this email already exists'})

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must match'})
        user.set_password(password)
        user.email = email
        user.save()
        Profile.objects.create(user=user)
        print(email)
        return user

# endregion


class loginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    
    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        user = authenticate(username=username, password=password)
        data = {}
        if user is not None:
            if user.is_active:
                data['username'] = username
                data['password'] = password
            else:
                data['respone'] = 'Account Disabled'
        else:
            data['respone'] = 'Account not valid'
        return data
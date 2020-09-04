from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics
from account.api.serializers import RegisterSerializer,loginSerializer
from django.contrib.auth.models import User
from account.models import Profile
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout



# region register user api

@api_view(['POST',])
def registerView(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            username = serializer.save()
            user = User.objects.get(username=username)
            data['respone'] = 'User created'
            data['username'] = user.username
            data['email'] = user.email
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

# endregion


# region log in user api

@api_view(['POST',])
def loginView(request):
    if request.method == 'POST':
        serializer = loginSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            userdata = serializer.save()
            user = authenticate(username = userdata['username'],password = userdata['password'])
            login(request,user)
            token = Token.objects.get(user=user).key
            data['token'] = token
            data['respone'] = 'User logged in'
        else:
            data = serializer.errors
        return Response(data)

# endregion

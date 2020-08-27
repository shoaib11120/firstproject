from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from ..models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User


# region Post detail

@api_view(['GET',])
def apiPostDetail(request,year,month,day,post):
    post=get_object_or_404(Post,
                        slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day,)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

# endregion



# region Post list

@api_view(['GET',])
def apiPostList(request):
    try:
        post=Post.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)

# endregion



# region Post Update

@api_view(['PUT',])
def apiPostDetailUpdate(request,year,month,day,post):
    post=get_object_or_404(Post,
                        slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day,)
    if request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Successfully Updated"
            return Response(data = data)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

# endregion



# region Post delete

@api_view(['DELETE',])
def apiPostDetailDelete(request,year,month,day,post):
    post=get_object_or_404(Post,
                        slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day,)
    if request.method == 'DELETE':
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "Successfully deleted"
        else:
            data["failed"] = "Delete unsuccessful"
        return Response(data = data)

# endregion



# region Post Create

@api_view(['POST',])
def apiPostDetailCreate(request):
    user = User.objects.get(pk=1)

    post=Post(author=user)

    if request.method == "POST":
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
# endregion


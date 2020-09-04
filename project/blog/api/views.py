from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404
from ..models import Post
from .serializers import PostSerializer
from django.contrib.auth.models import User


# region Post detail

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
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

class apiPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

# endregion



# region Post Update

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def apiPostDetailUpdate(request,year,month,day,post):
    post=get_object_or_404(Post,
                        slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day,)
    user = request.user
    if post.author != user:
        return Response({"Response":"Not allowed"})
    
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
@permission_classes((IsAuthenticated,))
def apiPostDetailDelete(request,year,month,day,post):
    post=get_object_or_404(Post,
                        slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day,)
    
    user = request.user
    if post.author != user:
        return Response({"Response":"Not allowed"})
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
@permission_classes((IsAuthenticated,))
def apiPostDetailCreate(request):
    post=Post(author=request.user)

    if request.method == "POST":
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
# endregion



from django.shortcuts import render
from  rest_framework.views import APIView
from .serializers import CreatePost, ListPost, UpdatePost
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.

class ListPostView(APIView):
  def get(self, request):
    all_post = Post.objects.all()
    serializer = ListPost(instance=all_post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class CreatePostView(APIView):
  def post(self, request):
    serializer = CreatePost(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  

class UpdatePostView(APIView):
  def put(self,request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = UpdatePost(data=request.data, instance=post)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)  


class DeletePostView(APIView):
  def delete(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


class DetailPostView(APIView):
  def get(self, request, post_id):
    post = get_object_or_404(Post, id=post_id, is_active=True)
    serializer = ListPost(instance=post)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer
from .models import PostComment
from rest_framework import permissions

# Create your views here.

class CommentViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'head', 'options']
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return PostComment.objects.filter(post_id=self.kwargs['post_pk'])


class ListCommentViewSet(ModelViewSet):
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAdminUser]


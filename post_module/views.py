from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import PostSerializer, LinkSerializer, FileSerializer, LinkBoxSerializer, CommentSerializer
from .models import Post, PostComment
from post_files.models import File
from utils.pagination import DefaultPagination
from post_links.models import Link, LinkBox
from utils.permissions import IsAdminOrReadOnly


# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('collection').all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['collection_id', 'is_recommend', 'status']
    search_fields = ['title', 'description', 'collection__title']
    ordering_fields = ['title', 'updated_at', 'created_at']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]


class LinkBoxViewSet(ModelViewSet):
    serializer_class = LinkBoxSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return LinkBox.objects.prefetch_related('links').filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}


class LinkViewSet(ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Link.objects.filter(post_id=self.kwargs['post_pk'], link_box_id=self.kwargs['linksbox_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk'],
                'link_box_id': self.kwargs['linksbox_pk']}


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return File.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}


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

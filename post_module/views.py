from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Count
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CollectionSerializer, LinkSerializer, FileSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Collection, File
from .pagination import DefaultPagination
from links.models import Link
# Create your views here.


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('collection').all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['collection_id']
    search_fields = ['title', 'description', 'collection__title']
    ordering_fields = ['title', 'last_update', 'created_at']
    pagination_class = DefaultPagination


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(posts_count=Count('posts')).all()
    serializer_class = CollectionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['parent_id']
    search_fields = ['title']
    ordering = ['title']
    pagination_class = DefaultPagination

    def destroy(self, request, *args, **kwargs):
        if Post.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it is associated with an Post'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)


class LinkViewSet(ModelViewSet):

    serializer_class = LinkSerializer

    def get_queryset(self):
        return Link.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}


class FileViewSet(ModelViewSet):

    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}

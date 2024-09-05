from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, DetailPostSerializer
from .models import Post
from utils.pagination import DefaultPagination
from utils.permissions import IsAdminOrReadOnly


# Create your views here.


class PostViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['collection', 'is_recommend', 'status']
    search_fields = ['title', 'collection__title', 'description',]
    ordering_fields = ['title', 'updated_at', 'created_at']
    # pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Post.objects.select_related('collection').prefetch_related('links_box', 'files').all()
        else:
            return Post.objects.select_related('collection').all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailPostSerializer
        else:
            return PostSerializer

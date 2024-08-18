from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Count
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, CollectionSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Collection
from .pagination import DefaultPagination
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
    queryset = Collection.objects.annotate(products_count=Count('posts')).all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request, *args, **kwargs):
        if Post.objects.filter(collection_id=kwargs['pk']).count() > 0:
          return Response({'error':'Collection cannot be deleted because it is associated with an Post'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
        return super().destroy(request, *args, **kwargs)

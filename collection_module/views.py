from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Collection
from .serializers import CollectionSerializer
from django.db.models.aggregates import Count
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.pagination import DefaultPagination
from utils.permissions import IsAdminOrReadOnly
from post_module.models import Post

# Create your views here.


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(posts_count=Count('posts')).all()
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['parent_id']
    search_fields = ['title']
    ordering = ['title']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        if Post.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it is associated with an Post'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *args, **kwargs)

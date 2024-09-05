from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import LinkBoxSerializer, LinkSerializer, ListLinkBoxSerializer
from .models import Link, LinkBox
from utils.permissions import IsAdminOrReadOnly
# Create your views here.


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
        if 'post_pk' in self.kwargs:
            return Link.objects.filter(post_id=self.kwargs['post_pk'], link_box_id=self.kwargs['linksbox_pk'])
        else:
            links_box = get_object_or_404(
                LinkBox, id=self.kwargs['linksbox_pk'])
            return Link.objects.filter(link_box_id=self.kwargs['linksbox_pk'], post_id=links_box.post.id)

    def get_serializer_context(self):
        if 'post_pk' in self.kwargs:
            return {'post_id': self.kwargs['post_pk'],
                    'link_box_id': self.kwargs['linksbox_pk']}
        else:
            links_box = get_object_or_404(
                LinkBox, id=self.kwargs['linksbox_pk'])

            return {'post_id': links_box.post.id,
                    'link_box_id': self.kwargs['linksbox_pk']}


class ListLinkBoxViewSet(ModelViewSet):
    queryset = LinkBox.objects.prefetch_related(
        'links').select_related('post').all()
    serializer_class = ListLinkBoxSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['post']
    search_fields = ['title','post__title']
    # permission_classes = [permissions.IsAdminUser]

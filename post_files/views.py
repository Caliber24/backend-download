from rest_framework.viewsets import ModelViewSet
from .models import File
from .serializers import FileSerializer
from utils.permissions import IsAdminOrReadOnly
# Create your views here.


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return File.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}

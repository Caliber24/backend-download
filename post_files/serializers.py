from rest_framework.serializers import ModelSerializer
from .models import File


class SimpleFileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['title', 'file']


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'title', 'file', 'post_id']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return File.objects.create(post_id=post_id, **validated_data)

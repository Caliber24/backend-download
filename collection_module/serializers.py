from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Collection


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count', 'parent']

    posts_count = serializers.IntegerField(read_only=True)

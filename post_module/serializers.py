from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post, Collection, File
from links.models import Link

from rest_framework import serializers


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'short_description',
                  'description', 'is_active', 'created_at', 'last_update', 'collection']


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

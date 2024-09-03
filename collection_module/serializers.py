from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import Collection


class SimpleCollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class CollectionSerializer(ModelSerializer):
    parent_title = SerializerMethodField(method_name='parent__title')

    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count',
            'parent', 'parent_title']

    posts_count = serializers.IntegerField(read_only=True)

    def parent__title(self, parent: Collection):
        return parent.title


class DetailCollectionSerializer(ModelSerializer):
    children = SimpleCollectionSerializer(read_only=True, many=True)
    parent_title = SerializerMethodField(method_name='parent__title')
    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count', 'parent','parent_title', 'children']

    posts_count = serializers.IntegerField(read_only=True)
    def parent__title(self, parent: Collection):
        return parent.title
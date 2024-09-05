from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import Collection


class SimpleCollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class CollectionSerializer(ModelSerializer):
    sub_collections = SimpleCollectionSerializer(read_only=True, many=True)
    parent_title = SerializerMethodField(method_name='parent__title')

    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count',
                  'parent', 'parent_title', 'sub_collections']

    posts_count = serializers.IntegerField(read_only=True)

    def parent__title(self, collection: Collection):
        if collection.parent:
            return collection.parent.title
        else :
            pass
            

class DetailCollectionSerializer(ModelSerializer):
    sub_collections = SimpleCollectionSerializer(many=True)
    parent_title = SerializerMethodField(method_name='parent__title')

    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count',
                  'parent', 'parent_title', 'sub_collections']

    posts_count = serializers.IntegerField(read_only=True)

    def parent__title(self, parent: Collection):
        return parent.title

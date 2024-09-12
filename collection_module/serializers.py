from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers

from .models import Collection





class SimpleCollectionSerializer(ModelSerializer):
    sub_collections = SerializerMethodField(method_name='get_sub_collections')
    
    class Meta:
        model = Collection
        fields = ['id', 'title', 'sub_collections']

    def get_sub_collections(self, collection:Collection):
        return SimpleCollectionSerializer(collection.sub_collections.all(), many=True).data

class CollectionSerializer(ModelSerializer):
    sub_collections = SimpleCollectionSerializer(read_only=True, many=True) 
    parent_title = SerializerMethodField(method_name='parent__title')

    class Meta:
        model = Collection
        fields = ['id', 'title',
                  'parent', 'parent_title', 'sub_collections']


    def parent__title(self, collection: Collection):
        if collection.parent:
            return collection.parent.title
        else:
            return

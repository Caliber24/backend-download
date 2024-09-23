from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post
from collection.models import Collection
from links.serializers import  SimpleLinkBoxSerializer
from rest_framework import serializers


class PostSerializer(ModelSerializer):
    collection_title = SerializerMethodField(
        method_name='collection__title', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image','file', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'collection', 'collection_title', 'status']

    def collection__title(self, post: Post):
        if post.collection:
            return post.collection.title
            


class DetailPostSerializer(ModelSerializer):
    links_box = SimpleLinkBoxSerializer(many=True, read_only=True)
    collection_title = SerializerMethodField(method_name='collection__title', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'links_box', 'file', 'collection', 'collection_title', 'status']

    def collection__title(self, post:Post):
        if post.collection:
            return post.collection.title
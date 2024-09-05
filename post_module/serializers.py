from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post
from collection_module.models import Collection
from post_links.serializers import  SimpleLinkBoxSerializer
from post_files.serializers import SimpleFileSerializer
from post_comments.serializers import CommentSerializer


from rest_framework import serializers


class PostSerializer(ModelSerializer):
    collection_title = SerializerMethodField(
        method_name='collection__title', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'collection', 'collection_title', 'status']

    def collection__title(self, post: Post):
        return post.collection.title


class DetailPostSerializer(ModelSerializer):
    files = SimpleFileSerializer(read_only=True, many=True)
    links_box = SimpleLinkBoxSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    collection_title = SerializerMethodField(method_name='collection__title', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'links_box', 'files', 'collection', 'collection_title', 'status', 'comments']

    def collection__title(self, post:Post):
        return post.collection.title

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post, PostComment
from post_files.models import File
from post_links.models import Link, LinkBox
from collection_module.serializers import CollectionSerializer

from rest_framework import serializers


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'collection', 'status']


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'link', 'link_box_id', 'post_id']

    def create(self, validated_data):
        post_id = self.context['post_id']
        link_box_id = self.context['link_box_id']
        return Link.objects.create(post_id=post_id, link_box_id=link_box_id, **validated_data)


class SimpleLinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'link']


class LinkBoxSerializer(ModelSerializer):
    links = SimpleLinkSerializer(many=True, read_only=True)

    class Meta:
        model = LinkBox
        fields = ['id', 'title', 'post_id', 'links']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return LinkBox.objects.create(post_id=post_id, **validated_data)


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['title', 'file', 'post_id']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return File.objects.create(post_id=post_id, **validated_data)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'post', 'parent', 'user', 'created_at', 'text']


class SimpleLinkBoxSerializer(ModelSerializer):
    links = SimpleLinkSerializer(many=True, read_only=True)

    class Meta:
        model = LinkBox
        fields = ['id', 'title', 'links']


class SimpleFileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ['title', 'file']


class PostDetailSerializer(ModelSerializer):
    files = SimpleFileSerializer(read_only=True, many=True)
    links_box = SimpleLinkBoxSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True)
    

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_recommend', 'created_at', 'updated_at', 'links_box', 'files', 'collection', 'status', 'comments']

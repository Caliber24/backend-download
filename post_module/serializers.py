from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post, Collection, File
from links.models import Link

from rest_framework import serializers



class CreatePost(ModelSerializer):
    class Meta:

        model = Post
        fields = ('__all__')


class ListPost(ModelSerializer):
    files = SerializerMethodField('get_files')
    links = SerializerMethodField('get_links')
    collection_title = SerializerMethodField('get_collection_title')

    class Meta:
        model = Post
        fields = "__all__"
        extra_fields = ['collection_title', 'files', 'links']

    def get_collection_title(self, post):
        collection = Collection.objects.get(id=post.collection.id)
        return collection.title

    def get_files(self, post):
        files = File.objects.filter(
            post_id=post.id).values_list('file', flat=True)
        return files

    def get_links(self, post):
        links = Link.objects.filter(
            post_id=post.id).values_list('title', 'link')
        return links


class UpdatePost(ModelSerializer):
    files = SerializerMethodField('get_files')
    links = SerializerMethodField('get_links')
    collection_title = SerializerMethodField('get_collection_title')
    class Meta:
        model = Post
        fields = ('title', 'image', 'short_description',
                  'description', 'is_active', 'collection_title', 'files', 'links')

    def get_files(self, post):
        files = File.objects.filter(
            post_id=post.id).values_list('file', flat=True)
        return files

    def get_links(self, post):
        links = Link.objects.filter(
            post_id=post.id).values_list('title', 'link')
        return links

    def get_collection_title(self, post):
        collection = Collection.objects.get(id=post.collection.id)
        return collection.title

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import Post, Collection, File
from links.models import Link, LinkBox

from rest_framework import serializers


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'posts_count', 'parent']

    posts_count = serializers.IntegerField(read_only=True)


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'short_description',
                  'description', 'is_active', 'created_at', 'last_update', 'collection']



class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields=['id','title','link','link_box_id','post_id'] 
    
    def create(self, validated_data):
        post_id = self.context['post_id']
        link_box_id=self.context['link_box_id']
        return Link.objects.create(post_id=post_id, link_box_id=link_box_id, **validated_data)
    

class SimpleLinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields=['id','title', 'link']         

class LinkBoxSerializer(ModelSerializer):
    
    links = SimpleLinkSerializer(many=True, read_only=True)
    class Meta:
        model=LinkBox
        fields=['id','title', 'post_id','links']
    
    def create(self, validated_data):
        post_id = self.context['post_id']
        return LinkBox.objects.create(post_id=post_id, **validated_data)



class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields=['title','file','post_id'] 
    
    def create(self, validated_data):
        post_id = self.context['post_id']
        return File.objects.create(post_id=post_id, **validated_data)
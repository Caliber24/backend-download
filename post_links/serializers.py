from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Link, LinkBox
from post_module.models import Post


class SimpleLinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'link']


class SimpleLinkBoxSerializer(ModelSerializer):
    links = SimpleLinkSerializer(many=True, read_only=True)

    class Meta:
        model = LinkBox
        fields = ['id', 'title', 'links']


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'title', 'link', 'link_box_id', 'post_id']

    def create(self, validated_data):
        post_id = self.context['post_id']
        link_box_id = self.context['link_box_id']
        return Link.objects.create(post_id=post_id, link_box_id=link_box_id, **validated_data)


class LinkBoxSerializer(ModelSerializer):
    links = SimpleLinkSerializer(many=True, read_only=True)

    class Meta:
        model = LinkBox
        fields = ['id', 'title', 'post_id', 'links']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return LinkBox.objects.create(post_id=post_id, **validated_data)



class ListLinkBoxSerializer(ModelSerializer):
    links = SimpleLinkSerializer(many=True, read_only=True)
    post_title = SerializerMethodField(method_name='post__title', read_only=True)
    class Meta:
        model = LinkBox
        fields = ['id', 'title', 'post', 'post_title', 'links']
    
    def post__title(self, link_box:LinkBox):
        return link_box.post.title
    
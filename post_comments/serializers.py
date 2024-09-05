from rest_framework.serializers import ModelSerializer
from .models import PostComment
class CommentSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'post', 'parent', 'user', 'created_at', 'text']
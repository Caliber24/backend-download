from rest_framework.serializers import ModelSerializer
from .models import Post

class CreatePost(ModelSerializer):
  class Meta:
    
    model=Post
    fields=('__all__')
    
class ListPost(ModelSerializer):
  
  class Meta:
    model = Post
    fields=("__all__")
    

class UpdatePost(ModelSerializer):
  class Meta:
    model=Post
    fields=('title','image','description')
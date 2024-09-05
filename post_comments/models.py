from django.db import models
from django.conf import settings
from post_module.models import Post
# Create your models here.

class PostComment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'PostComment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.post.title}'
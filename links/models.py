from django.db import models
from post_module.models import Post
# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان لینک')
    link = models.URLField(verbose_name='لینک')
    post = models.ForeignKey(Post, models.CASCADE,verbose_name='پست')

    def __str__(self) -> str:
        return self.title
    class Meta:
      verbose_name = 'لینک'
      verbose_name_plural = 'لینک‌ها'
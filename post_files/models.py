from django.db import models
from post_module.models import Post


# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان فایل')
    file = models.FileField(upload_to='files/post',
                            null=True, blank=True, verbose_name='فایل')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل‌ها'

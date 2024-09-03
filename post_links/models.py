from django.db import models
from post_module.models import Post


# Create your models here.

class LinkBox(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان باکس لینک')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='پست', related_name='links_box')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'باکس لینک'
        verbose_name_plural = 'باکس‌های دانلود'


class Link(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان لینک')
    link = models.URLField(verbose_name='لینک')
    link_box = models.ForeignKey(LinkBox, models.CASCADE, verbose_name='باکس لینک', related_name='links')
    post = models.ForeignKey(Post, models.CASCADE, verbose_name='پست')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک‌ها'

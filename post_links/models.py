from django.db import models
from post_module.models import Post


# Create your models here.

class LinkBox(models.Model):
    title = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='links_box')

    def __str__(self):
        return self.title



class Link(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    link_box = models.ForeignKey(LinkBox, models.CASCADE,related_name='links')
    post = models.ForeignKey(Post, models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


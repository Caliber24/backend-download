from django.db import models
from collection.models import Collection
from django.conf import settings
from django.urls import reverse


# Create your models here.

# def upload_to(instance, filename):
#     return 'images/post/{filename}'.format(filename=filename)





class Post(models.Model):
    STATUS_CHOICES = [
        (0, 'Disable'),
        (1, 'Active'),
        (2, 'Pending')
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/post', null=True, blank=True)
    file = models.FileField(upload_to='files/post', null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField()
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, related_name='posts', null=True, blank=True)
    status = models.PositiveSmallIntegerField(
        default=2, choices=STATUS_CHOICES)  # 0=disable, 1=active, 2=pending
    is_recommend = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.title
    

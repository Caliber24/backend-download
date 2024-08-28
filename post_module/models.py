from django.db import models
from collection_module.models import Collection
from django.conf import settings
from django.urls import reverse


# Create your models here.

# def upload_to(instance, filename):
#     return 'images/post/{filename}'.format(filename=filename)


class Post(models.Model):
    STATUS_CHOICES = [
        ('Disable', 0),
        ('Active', 1),
        ('Pending', 2)
    ]

    title = models.CharField(max_length=255, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/post',
                              verbose_name='تصویر پست', null=True, blank=True)
    short_description = models.TextField(
        verbose_name='متن کوتاه', null=True, blank=True)
    description = models.TextField(verbose_name='متن')
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='posts', verbose_name=("دسته‌بندی"), null=True, blank=True)
    status = models.PositiveSmallIntegerField(
        default=2, choices=STATUS_CHOICES)  # 0=disable, 1=active, 2=pending
    is_recommend = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True ,verbose_name='ساخته شده در')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='ویرایش شده در')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'

    def __str__(self):
        return self.title


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('PostComment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return str(self.user) + self.post.title

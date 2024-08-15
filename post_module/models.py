from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/post',
                              verbose_name='تصویر پست', null=True, blank=True)
    description = models.TextField(verbose_name='متن')
    # slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    collection = models.models.ForeignKey(
        Collection, verbose_name=("دسته‌بندی"), on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    link = models.CharField(max_length=1000, verbose_name='متن لینک')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک‌ها'


class File(models.Model):
    file = models.FileField(upload_to='files/post',
                            null=True, blank=True, verbose_name='فایل')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

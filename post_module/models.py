from django.db import models
from django.urls import reverse
from jalali_date import date2jalali
# Create your models here.

# def upload_to(instance, filename):
#     return 'images/post/{filename}'.format(filename=filename)

class Collection(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان دسته‌بندی')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children', verbose_name='ابردسته‌بندی')
    featured_post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True,
                                      blank=True, verbose_name='پست‌های دسته‌بندی', related_name='+')

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
    short_description = models.TextField(
        verbose_name='متن کوتاه', null=True, blank=True)
    description = models.TextField(verbose_name='متن')
    # slug = models.SlugField(unique=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.PROTECT, verbose_name=("دسته‌بندی"), null=True, blank=True)

    is_active = models.BooleanField(default=False, verbose_name='فعال')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='ساخته شده در')
    last_update = models.DateTimeField(
        auto_now=True, verbose_name='ویرایش شده در')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست‌ها'

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to='files/post',
                            null=True, blank=True, verbose_name='فایل')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل‌ها'

from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/post',
                              verbose_name='تصویر پست',null=True, blank=True)
    description = models.TextField(verbose_name='متن')
    slug = models.SlugField()
    File = models.FileField(upload_to=('Files/post'), null=True, blank=True,
                             verbose_name='فایل های پست')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    link = models.CharField(max_length=1000,verbose_name='متن لینک')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک‌ها'
    
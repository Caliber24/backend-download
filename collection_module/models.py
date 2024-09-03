from django.db import models


# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان دسته‌بندی')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True,related_name='children', verbose_name='ابردسته‌بندی')
    is_active = models.BooleanField(default=False, verbose_name='فعال')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'

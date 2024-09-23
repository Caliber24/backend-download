from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               blank=True, related_name='sub_collections')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
  list_display = ['title', 'link', 'post']
  list_editable=[ 'link', 'post']
  autocomplete_fields = ['post']
  list_filter=['post']
  ordering=['post','title']
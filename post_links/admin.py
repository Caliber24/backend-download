from django.contrib import admin

from . import models
# Register your models here.

class LinkInline(admin.TabularInline):
    model = models.Link
    min_num = 0
    extra = 0

@admin.register(models.Link)
class LinkAdmin(admin.ModelAdmin):
  list_display = ['title', 'link', 'post']
  list_editable=[ 'link', 'post']
  autocomplete_fields = ['post']
  list_filter=['post']
  ordering=['post','title']



@admin.register(models.LinkBox)
class LinkBoxAdmin(admin.ModelAdmin):
  list_display = ['title']
  inlines = [LinkInline]
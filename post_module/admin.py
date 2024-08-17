from typing import Any
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
# from django.db.models.query import QuerySet
from .models import Post, Collection, File
from links.models import Link
from jalali_date import datetime2jalali, date2jalali


class LinkInline(admin.TabularInline):
  model=Link
  min_num=0
  extra=0
  
class FileInline(admin.TabularInline):
  model = File
  min_num=0
  max_num=3
  extra=0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display=['title','collection','get_created_jalali','get_update_jalali','is_active']
  list_editable=['is_active']
  autocomplete_fields=['collection']
  search_fields=['title']
  list_filter=['collection','last_update']
  list_per_page = 10
  list_select_related = ['collection']
  inlines=[LinkInline, FileInline]
  
  @admin.display(description='تاریخ ایجاد', ordering='created_at')
  def get_created_jalali(self, post):
    return datetime2jalali(post.created_at).strftime('%a, %d %b %Y %H:%M:%S')
  
  @admin.display(description='تاریخ ویرایش', ordering='created_at')
  def get_update_jalali(self, post):
    return datetime2jalali(post.last_update).strftime('%a, %d %b %Y %H:%M:%S')



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
  list_display=['title','parent','posts_count']
  list_editable=['parent']
  search_fields=['title']
  autocomplete_fields=['parent','featured_post']
  ordering = ['title']
  list_filter = ['parent']
  list_select_related=['parent']
  
  @admin.display(description='تعداد پست', ordering='posts_count')
  def posts_count(self,collection):
    url=(reverse('admin:post_module_post_changelist')
         + '?'
         +urlencode({
           'collection_id':str(collection.id)
         }))
    return format_html("<a href='{}'>{}</a>", url, collection.posts_count)
  
  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      posts_count=Count('post')
    )
  
  

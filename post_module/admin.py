from typing import Any
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models.aggregates import Count
# from django.db.models.query import QuerySet
from .models import Post, PostComment
from post_files.models import File
from post_links.models import Link


class LinkInline(admin.TabularInline):
    model = Link
    min_num = 0
    extra = 0


class FileInline(admin.TabularInline):
    model = File
    min_num = 0
    max_num = 3
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'updated_at', 'created_at', 'status', 'is_recommend']
    list_editable = ['status', 'is_recommend']
    autocomplete_fields = ['collection']
    search_fields = ['title']
    list_filter = ['collection', 'updated_at']
    list_per_page = 10
    list_select_related = ['collection']
    inlines = [LinkInline, FileInline]


admin.site.register(PostComment)

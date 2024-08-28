from django.contrib import admin
from .models import Collection


# Register your models here.

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']
    search_fields = ['title']
    autocomplete_fields = ['parent']
    ordering = ['title']
    list_filter = ['parent']
    list_select_related = ['parent']

    # @admin.display(description='تعداد پست', ordering='posts_count')
    # def posts_count(self,collection):
    #   url=(reverse('admin:post_module_post_changelist')
    #        + '?'
    #        +urlencode({
    #          'collection_id':str(collection.id)
    #        }))
    #   return format_html("<a href='{}'>{}</a>", url, collection.posts_count)

    # def get_queryset(self, request):
    #   return super().get_queryset(request).annotate(
    #     posts_count=Count('post')
    #   )


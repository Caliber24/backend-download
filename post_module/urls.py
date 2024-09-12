from django.urls import path
from rest_framework_nested import routers
from . import views as post_views
from collection_module import views as collection_views
from post_links import views as link_views
from post_comments import views as comment_views

router = routers.DefaultRouter()
router.register('posts', post_views.PostViewSet, basename='posts')
router.register('collections', collection_views.CollectionViewSet)
router.register('comments', comment_views.ListCommentViewSet)
router.register('linksboxes', link_views.ListLinkBoxViewSet)
router.register('create-links', link_views.CreateLinkViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('linksboxes', link_views.LinkBoxViewSet,
                      basename='posts-linksboxes')
posts_router.register('comments', comment_views.CommentViewSet,
                      basename='posts-comments')

posts_router2 = routers.NestedDefaultRouter(
    posts_router, 'linksboxes', lookup='linksbox')
posts_router2.register('links', link_views.LinkViewSet,
                       basename='posts-linksboxes-links')

linksbox_router = routers.NestedDefaultRouter(
    router, 'linksboxes', lookup='linksbox')
linksbox_router.register('links', link_views.LinkViewSet,
                         basename='linksboxes-links')

urlpatterns = router.urls + posts_router.urls + \
    posts_router2.urls + linksbox_router.urls

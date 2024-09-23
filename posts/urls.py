from django.urls import path
from rest_framework_nested import routers
from . import views as post_views
from collection import views as collection_views
from links import views as link_views

router = routers.DefaultRouter()
router.register('posts', post_views.PostViewSet, basename='posts')
router.register('collections', collection_views.CollectionViewSet)
router.register('linksboxes', link_views.ListLinkBoxViewSet)
router.register('create-links', link_views.CreateLinkViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('linksboxes', link_views.LinkBoxViewSet,
                      basename='posts-linksboxes')

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

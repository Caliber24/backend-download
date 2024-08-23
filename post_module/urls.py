from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('posts',views.PostViewSet, basename='posts')
router.register('collections', views.CollectionViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('linksboxes', views.LinkBoxViewSet, basename='posts-linksboxes')
posts_router.register('files', views.FileViewSet, basename='posts-files')

posts_router2 = routers.NestedDefaultRouter(posts_router,'linksboxes',lookup='linksbox')
posts_router2.register('links',views.LinkViewSet,basename='posts-linksboxes-links')

urlpatterns = router.urls + posts_router.urls + posts_router2.urls




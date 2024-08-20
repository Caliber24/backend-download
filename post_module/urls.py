from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('posts',views.PostViewSet, basename='posts')
router.register('collections', views.CollectionViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('links', views.LinkViewSet, basename='posts-links')
posts_router.register('files', views.FileViewSet, basename='posts-files')

urlpatterns = router.urls + posts_router .urls




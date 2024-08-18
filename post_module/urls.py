from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('posts',views.PostViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls 




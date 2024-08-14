from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create_post')
]

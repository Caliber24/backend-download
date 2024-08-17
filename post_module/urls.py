from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.CreatePostView.as_view(), name='create_post'),
    path('list/',views.ListPostView.as_view(), name='list_post'),
    path('update/<post_id>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<post_id>', views.DeletePostView.as_view(), name='delete_post'),
    path("detail/<int:post_id>", views.DetailPostView.as_view(), name="detail_post")
]

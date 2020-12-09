
from django.urls import path, include


from .views import (
    post_create_view,
    post_list_view,
    post_delete_view,
    post_detail_view
)

urlpatterns = [

    path('',post_list_view,name='post-read'),
    path('create/',post_create_view,name='post-create'),
    path('<int:post_id>/',post_detail_view,name='post-detail'),
    path('<int:post_id>/delete/',post_delete_view,name='post-delete'),
]

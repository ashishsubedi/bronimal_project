
from django.urls import path, include


from .views import (
    post_create_view,
    post_list_view,
)

urlpatterns = [

    path('',post_list_view,name='post-read'),
    path('create/',post_create_view,name='post-create'),
]

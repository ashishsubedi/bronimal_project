
from django.urls import path, include


from .views import (
    post_create_view,
    post_list_view,
    post_delete_view,
    post_detail_view,
    comment_create_view,
    like_toggle_view,

    PostListView,
    PostDetailView,
    CommentListView,
    LikeListView,
    PostUpdateView,
    PostDeleteView,
    CommentUpdateView,
    CommentDeleteView,
    UserPostListView

)

urlpatterns = [

    # path('',post_list_view,name='post-list'),
    path('',PostListView.as_view(),name='post-list'),
    path('create/',post_create_view,name='post-create'),
    path('<str:username>/',UserPostListView.as_view(),name='post-user-view'),
    # path('post/<int:post_id>/',post_detail_view,name='post-detail'),
    path('post/<int:post_id>/',PostDetailView.as_view(),name='post-detail'),
    path('<int:post_id>/update/',PostUpdateView.as_view(),name='post-update'),
    # path('<int:post_id>/delete/',post_delete_view,name='post-delete'),
    path('<int:post_id>/delete/',PostDeleteView.as_view(),name='post-delete'),
    #Comments
    path('<int:post_id>/comments/create/',comment_create_view,name='comment-create'),
    path('<int:post_id>/comments/',CommentListView.as_view(),name='post-comments'),
    path('<int:post_id>/comments/<int:comment_id>/update/',CommentUpdateView.as_view(),name='comment-update'),
    path('<int:post_id>/comments/<int:comment_id>/delete/',CommentDeleteView.as_view(),name='comment-delete'),

    #Likes
    path('<int:post_id>/likes/toggle/',like_toggle_view,name='likes-toggle'),
    path('<int:post_id>/likes/',LikeListView.as_view(),name='post-likes'),
]

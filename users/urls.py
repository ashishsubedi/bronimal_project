
from django.urls import path, include


from .views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,

    ProfileDetailView

)

urlpatterns = [

    path('register/',UserCreateView.as_view(),name='user-register'),
    path('<str:username>/',UserDetailView.as_view(),name='user-detail'),
    path('<str:username>/update/',UserUpdateView.as_view(),name='user-update'),
    path('<str:username>/delete/',UserDeleteView.as_view(),name='user-delete'),
    
    path('profile/<str:username>/',ProfileDetailView.as_view(),name='user-profile-detail'),

]

from django.shortcuts import render

from .models import Profile,User


from .serializers import (
    ProfileCreateSerializer,
    ProfileSerializer,
    UserSerializer,
    UserCreateSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated
)
from .permissions import (
    IsOwnerOrReadOnly
)

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    

)

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)

    return Response(serializer.data,status=200)


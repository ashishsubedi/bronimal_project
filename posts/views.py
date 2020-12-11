from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import (PostSerializer, PostCreateSerializer,PostDetailSerializer)

from rest_framework.generics import (RetrieveAPIView)

@api_view(['GET'])
def post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)

    return Response(serializer.data,status=200)

@api_view(['POST'])
def post_create_view(request):
    serializer = PostCreateSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)

        return Response(serializer.data,status=201)
    return Response({'message':"ERROR"},status=404)
    
@api_view(['GET'])
def post_detail_view(request,post_id):
    post = Post.objects.filter(id=post_id)

    if not post.exists():
        return Response({"message":"Post doesn't exist"},status=404)
    print(post.values())
    serializer = PostSerializer(post,many=True)

    return Response(serializer.data,status=200)
    
class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_url_kwarg = 'post_id'

@api_view(['DELETE','POST'])
def post_delete_view(request,post_id):
    post = Post.objects.filter(id=post_id)
    if not post.exists():

        return Response({"message":"Post doesn't exist"},status=404)
    post = post.filter(author=request.user)
    if not post.exists():
        return Response({"message":"You cannot delete this post"},status=403)
    post = post.first()
    post.delete()
    return Response({'message':"Deleted Post"},status=204)


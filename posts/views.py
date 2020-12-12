from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment, Like
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostDetailSerializer,
    CommentSerializer,   
    LikeSerializer  
)
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
    # UpdateCreateAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView

)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)

    return Response(serializer.data,status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def post_create_view(request):
    serializer = PostCreateSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)

        return Response(serializer.data,status=201)
    return Response({'message':"ERROR"},status=404)
    
class PostUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

class PostDeleteView(RetrieveDestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
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
    permission_classes = [IsAuthenticated]


@api_view(['DELETE','POST'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def post_delete_view(request,post_id):
    post = Post.objects.filter(id=post_id)
    if not post.exists():

        return Response({"message":"Post doesn't exist"},status=404)
    post = post.filter(user=request.user)
    if not post.exists():
        return Response({"message":"You cannot delete this post"},status=403)
    post = post.first()
    post.delete()
    return Response({'message':"Deleted Post"},status=204)

# For Comments

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def comment_create_view(request,post_id):
    post = Post.objects.filter(id=post_id)
    if not post.exists():

        return Response({"message":"Post doesn't exist"},status=404)

    post = post.first()

    obj = post.comments.create(user=request.user,comment=request.data['comment'])
    print(obj)
    return Response({
        'message':"Comment created",
        'data':CommentSerializer(obj).data
    },status=201)

class CommentUpdateView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]



class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

 

#For likes

class LikeListView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_url_kwarg = 'post_id'
    permission_classes = [IsAuthenticated]


    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,IsOwnerOrReadOnly])
def like_toggle_view(request,post_id):
    post = Post.objects.filter(id=post_id)
    if not post.exists():
        return Response({"message":"Post doesn't exist"},status=404)

    post = post.first()
   
    obj = post.likes.create(user=request.user)
    return Response({
        'message':"Success",
       
    },status=201)
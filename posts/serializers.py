from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','comment','timestamp']

class PostCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post
        fields = ['id','caption','likes','timestamp','image']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = ['id','author','caption','likes','timestamp','image','comments']


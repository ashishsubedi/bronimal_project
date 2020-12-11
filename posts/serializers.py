from rest_framework import serializers
from .models import Post,Comment,Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','user','comment','timestamp']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','user','post','timestamp']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','caption','timestamp','image']

    def get_likes(self,obj):
        return obj.likes.count()

class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','author','caption','likes','timestamp','image','comments']

    def get_likes(self,obj):
        return obj.likes.count()
    
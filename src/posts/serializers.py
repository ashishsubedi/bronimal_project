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


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    
    comments = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Post
        fields = ['id','user','caption','image','likes','comments','likes_count','comments_count','timestamp']

    def get_likes_count(self,obj):
        return obj.likes.count()

    def get_comments_count(self,obj):
        return obj.comments.count()

    def get_comments(self,obj):
        qs = obj.comments.filter()[:3]
        serialize = CommentSerializer(qs,many=True)
        return serialize.data

    def get_likes(self,obj):
        qs = obj.likes.filter()[:3]
        serialize = LikeSerializer(qs,many=True)
        return serialize.data



   
class PostDetailSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    likes = LikeSerializer(many=True,read_only=True)

    comments = CommentSerializer(many=True,read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    
    class Meta:
        model = Post
        fields = ['id','user','caption','image','likes','comments','likes_count','comments_count','timestamp']

    def get_likes_count(self,obj):
        return obj.likes.count()

    def get_comments_count(self,obj):
        return obj.comments.count()

    
    
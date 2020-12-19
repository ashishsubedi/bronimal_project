from rest_framework import serializers
from django.urls import reverse

from .models import Post,Comment,Like

from django.contrib.auth import get_user_model
User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    user_profile_url = serializers.SerializerMethodField(read_only=True)
    timestamp = serializers.DateTimeField(format="​%Y-%m-%d %H:%M")
    user_avatar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id','post','username','user_avatar','user_profile_url','comment','timestamp']
    def get_username(self,obj):
        return obj.user.username
    def get_user_profile_url(self,obj):
        return reverse('user-profile-detail', args=(obj.user.username,))
    def get_user_avatar(self,obj):
        return obj.user.profile.avatar.url

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    user_profile_url = serializers.SerializerMethodField(read_only=True)
    timestamp = serializers.DateTimeField(format="​%Y-%m-%d %H:%M")
    user_avatar = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Like
        fields = ['id','username','user_avatar','user_profile_url','post','timestamp']
    def get_username(self,obj):
        return obj.user.username
    def get_user_profile_url(self,obj):
        return reverse('user-profile-detail', args=(obj.user.username,))
    def get_user_avatar(self,obj):
        return obj.user.profile.avatar.url

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','caption','timestamp','image']


class PostSerializer(serializers.ModelSerializer):

    likes_count = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    
    comments = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    username = serializers.SerializerMethodField(read_only=True)
    user_profile_url = serializers.SerializerMethodField(read_only=True)
    user_avatar = serializers.SerializerMethodField(read_only=True)

    post_url = serializers.SerializerMethodField(read_only=True)
    timestamp = serializers.DateTimeField(format="​%Y-%m-%d %H:%M")


    class Meta:
        model = Post
        fields = ['id','username','user_profile_url','user_avatar','post_url','caption','image','likes','comments','likes_count','comments_count','timestamp']

    def get_username(self,obj):
        return obj.user.username
    def get_user_profile_url(self,obj):
        return reverse('user-profile-detail', args=(obj.user.username,))
    def get_user_avatar(self,obj):
        return obj.user.profile.avatar.url

    def get_post_url(self,obj):
        return reverse('post-detail',args=(obj.pk,))

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
    
    username = serializers.SerializerMethodField(read_only=True)
    user_profile_url = serializers.SerializerMethodField(read_only=True)
    user_avatar = serializers.SerializerMethodField(read_only=True)
    post_url = serializers.SerializerMethodField(read_only=True)

    timestamp = serializers.DateTimeField(format="​%Y-%m-%d %H:%M")

    
    class Meta:
        model = Post
        fields = ['id','username','user_profile_url','user_avatar','post_url','caption','image','likes','comments','likes_count','comments_count','timestamp']
    
    def get_username(self,obj):
        return obj.user.username

    def get_user_profile_url(self,obj):
        return reverse('user-profile-detail', args=(obj.user.username,))
    
    def get_user_avatar(self,obj):
        return obj.user.profile.avatar.url

    def get_post_url(self,obj):
        return reverse('post-detail',args=(obj.pk,))

    def get_likes_count(self,obj):
        return obj.likes.count()

    def get_comments_count(self,obj):
        return obj.comments.count()

    
    
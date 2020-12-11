from django.contrib import admin
from .models import Post,Comment,Like

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
class LikeInline(admin.TabularInline):
    model = Like
    extra = 1

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CommentInline,LikeInline]


admin.site.register(Post,PostAdmin)
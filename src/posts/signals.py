from django.dispatch import receiver
from .models import Like,Post
from users.models import User

from django.db.models.signals import post_save,pre_save

# @receiver(pre_save,sender=Like)
# def handle_like_dislike(sender,instance,created):
#     like,created = Like.objects.get_or_create(user=instance.user,post=instance.post)
#     if not created:
#         like.delete()
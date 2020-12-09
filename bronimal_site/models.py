from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    firstname = models.CharField(max_length=25,blank=True)
    lastname = models.CharField(max_length=25,blank=True)
    address = models.CharField(max_length=50,blank=True)
    bio = models.TextField(max_length=255,blank=True)
    dob = models.DateField(null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics',default='default.jpg')

    def __str__(self):
        return f'{self.user.username}'


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Post(models.Model):
    author = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    caption = models.TextField(blank=True,null=True,max_length=255)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)

    def save(self):
        super().save()

        img = Image.open(self.image.path)
    
        output_size = (400,400)
        img.thumbnail(output_size)
        img.save(self.image.path)

    


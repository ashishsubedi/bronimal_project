from django.db import models

# from django.contrib.auth.models import User
from users.models import User
from PIL import Image

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)

    class Meta:
        ordering = ['-timestamp']

class Like(models.Model):
    post = models.ForeignKey('Post',related_name='likes',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def save(self,*args,**kwargs):
        qs = Like.objects.filter(user=self.user,post=self.post)

        if qs.exists():
            qs.delete()
        else:
            super().save()
        

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    caption = models.TextField(blank=True,max_length=255)
    image = models.ImageField(upload_to='images',blank=True)
   
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-timestamp']

    def save(self,*args,**kwargs):
        
        if self.image:
            img = Image.open(self.image)
        
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if not self.image and not self.caption:
            raise ValueError("Provide either caption or image")
        
        super().save()

    
    


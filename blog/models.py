from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    parent_id = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return '%s' % (self.name)

class Tag(models.Model):
    name = models.CharField(max_length=100, null= False, blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    message = models.TextField( null=False, blank=False)
    user_name =models.CharField(max_length=100, blank=True, null=True)
    user_email =models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    title= models.CharField(max_length=200,null=False, blank=False)
    post = models.TextField(null=False, blank=False)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    likes = models.IntegerField(null=False, blank=False)
    views = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return '%s' % (self.title)

class Comment(models.Model):

    rating= models.IntegerField(null=False, blank=False)  
    content = models.TextField(null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Image(models.Model):

    imag_url= models.CharField(max_length=200,null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Share(models.Model):
    SOCIAL_SITES = (
        ('F','Facebook'),
        ('T','Twitter'),
        ('I','Instragram'),
        ('L','Linkedin'),
        ('F','Facebook'),
        ('O','Other'),
    )

    social_media= models.CharField(choices=SOCIAL_SITES,max_length=200,null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
















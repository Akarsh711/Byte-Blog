from django.db import models
from django.contrib.auth.models import User
import datetime

class Tags(models.Model):
   tag = models.CharField(max_length=50)

   def __str__(self):
        return self.tag

class Category(models.Model):
    name = models.CharField(max_length=39)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    brief_description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length = 13)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    thumbnail = models.ImageField('thumbnails')
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.title +' '+ 'by' + '   @'+self.author



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=39)
    email = models.EmailField()
    subject = models.CharField(max_length=69)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)# subcomments
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    # comment = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)# subcomment
    
class FeaturedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    


    def __str__(self):
        return str(self.post.sno) + self.post.title


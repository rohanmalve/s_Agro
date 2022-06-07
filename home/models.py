from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=122)
    email=models.CharField( max_length=122)
    phone=models.CharField( max_length=12)
    desc=models.CharField(max_length=500)
    date=models.DateField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title
    def imagetag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))

# Post Model 
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=HTMLField()
    price=models.IntegerField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category ,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/')
    def __str__(self):
        return self.title
    def imagetag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))
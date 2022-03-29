from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=15)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Post(models.Model):
    author=models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    image=models.FileField()
    desc=RichTextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    terms_condition=RichTextField(null=True,blank=True)
    fraud_alert=RichTextField(null=True,blank=True)
    disclaimer=RichTextField(null=True,blank=True)
    privacy_policy=RichTextField(null=True,blank=True)
    faq=RichTextField(null=True,blank=True)
    





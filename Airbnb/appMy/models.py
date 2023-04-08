from django.db import models
from django.contrib.auth.models import User
from appUser.models import *
# Create your models here.


class Category(models.Model):
    name=models.CharField(("kategori ismi"), max_length=50)
    c_image=models.FileField(("kategori iconu"), upload_to=None, max_length=100, null=True)
    def __str__(self):
        return self.name
    

class House(models.Model):
    owner=models.ForeignKey(User, verbose_name=("Sahip"), on_delete=models.CASCADE)
    category=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    name=models.CharField(("ev ismi"), max_length=50)
    image=models.FileField(("ev gorseli"), upload_to=None, max_length=100, null=True)
    image1=models.FileField(("ev gorseli1"), upload_to=None, max_length=100, null=True)
    image2=models.FileField(("ev gorseli2"), upload_to=None, max_length=100, null=True)
    image3=models.FileField(("ev gorseli3"), upload_to=None, max_length=100, null=True)
    image4=models.FileField(("ev gorseli4"), upload_to=None, max_length=100, null=True)
    country=models.CharField(("ulke"), max_length=50)
    location=models.TextField(("konum"),max_length=100)
    publish_date=models.DateTimeField(("yayin tarihi"), auto_now=False, auto_now_add=False)
    price=models.IntegerField(("ucret"))
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    commenter=models.ForeignKey(User, verbose_name=("yorum yapan"), on_delete=models.CASCADE,null=True)
    house=models.ForeignKey(House, verbose_name=("ev"), on_delete=models.CASCADE)
    text=models.TextField(("yorum"),max_length = 150)
    
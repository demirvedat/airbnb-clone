from django.db import models
from django.contrib.auth.models import User
from appUser.models import *
# Create your models here.


class Category(models.Model):
    name=models.CharField(("kategori ismi"), max_length=50)
    def __str__(self):
        return self.name
    

class House(models.Model):
    owner=models.ForeignKey(User, verbose_name=("Sahip"), on_delete=models.CASCADE)
    category=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    name=models.CharField(("ev ismi"), max_length=50)
    image=models.FileField(("ev gorseli"), upload_to=None, max_length=100, null=True)
    country=models.CharField(("ulke"), max_length=50)
    location=models.TextField(("konum"),max_length=100)
    publish_date=models.DateTimeField(("yayin tarihi"), auto_now=False, auto_now_add=False)
    price=models.IntegerField(("ucret"))
    
    def __str__(self):
        return self.name
    
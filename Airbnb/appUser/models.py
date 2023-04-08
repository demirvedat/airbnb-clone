from django.db import models
from appMy.models import *
from django.contrib.auth.models import User
# Create your models here.
class Userinfo(models.Model):
    user=models.OneToOneField(User, verbose_name=("kullanici"), on_delete=models.CASCADE)
    name=models.CharField(("kullanici ismi"), max_length=50)
    join_date=models.DateTimeField(("katilim tarihi"), auto_now=False, auto_now_add=False)
    pr_image=models.FileField(("profil resmi"), upload_to=None, max_length=100)
    bio=models.TextField(("kullanici hakkinda"),max_length=150)
    

    def __str__(self):
        return self.name

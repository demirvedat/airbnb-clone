from django.shortcuts import render,redirect
from .models import *
from appUser.models import *
# Create your views here.
def Index(request):
    houses=House.objects.all()
    
    context={
        'houses':houses,
    }
    return render(request,'index.html',context)

def Detail(request,id):
    house=House.objects.get(id=id)
    comments=Comment.objects.filter(house=id)
    context={
        'house':house,
        'comments':comments,
    }
    return render(request,'detail.html',context)

def Sharehome(request):
    
    return render(request,'sharehome.html')

def Homeadd(request):
    
    return render(request,'homeadd.html')


def Profile(request,pk):
    houses=House.objects.all()
    user=User.objects.get(id=pk)
    comments=Comment.objects.all()
    context={
      'user':user,
      'houses':houses,  
      'comments':comments,
    }
   
    return render(request,'profile.html',context)

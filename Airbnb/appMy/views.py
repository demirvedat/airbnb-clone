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
    
    context={
        'house':house,
    }
    return render(request,'detail.html',context)

def Sharehome(request):
    return render(request,'sharehome.html')

def Profile(request,pk):
    houses=House.objects.all()
    user=User.objects.get(id=pk)
   
    context={
      
      'user':user,
      'houses':houses,  
    }
   
    return render(request,'profile.html',context)

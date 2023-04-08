from django.shortcuts import render,redirect,get_object_or_404
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
    categories=Category.objects.all()
    if 'addhome' in request.POST:
        housename=request.POST['housename']
        categoryid = request.POST['category']
        category = get_object_or_404(Category, id=categoryid)
        country=request.POST['country']
        location=request.POST['location']
        price=request.POST['price']
        date=request.POST['date']
        image=request.FILES['image']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        image4=request.FILES['image4']
        
        house=House(name=housename, category=category, country=country, location=location, price=price, publish_date=date, image=image, image1=image1, image2=image2, image3=image3,image4=image4, owner=request.user)
        house.save() 
        return redirect('Index')
    context={
        'categories':categories,
    }
    return render(request,'homeadd.html',context)


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

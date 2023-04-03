from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def loginUser(request):
    
    if 'loginer' in request.POST:
            
        username=request.POST['username']
        password=request.POST['password']
                
                
        user=authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
    return redirect('Index')
                
    
    

def registerUser(request):
   
    if 'registerer' in request.POST:
        name=request.POST['name']
        surname=request.POST['surname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
            
        if password1 == password2:
            user=User.objects.create_user(first_name=name,last_name=surname,username=username,email=email,password=password1)
            user.save()
    return redirect('Index')
    
            
def logoutUser(request):
    logout(request)
    return redirect('Index')
    
    

from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Detail(request):
    return render(request,'detail.html')

def Sharehome(request):
    return render(request,'sharehome.html')

def Profile(request):
    return render(request,'profile.html')

from django.shortcuts import render
from .models import Logo_Image,Contact_Info,Students_new
from django.http import HttpResponse

# Create your views here.
def index(request):
    data=Logo_Image.objects.all()
    pata=Contact_Info.objects.all()
    context = {
        'data':data,
        'pata':pata
    }
    
   
    return render(request,'index.html',context)

def about(request):
    data=Logo_Image.objects.all()
    pata=Contact_Info.objects.all()
    kata=Students_new.objects.all()
    context = {
        'data':data,
        'pata':pata,
        'kata':kata
    }
    return render(request,'about.html',context)
def services(request):
    data=Logo_Image.objects.all()
    pata=Contact_Info.objects.all()
    kata=Students_new.objects.all()
    context = {
        'data':data,
        'pata':pata,
        'kata':kata
    }
    return render(request,'services.html',context)
    
def contact(request):
    data=Logo_Image.objects.all()
    pata=Contact_Info.objects.all()
    kata=Students_new.objects.all()
    context = {
        'data':data,
        'pata':pata,
        'kata':kata
    }
    return render(request,'contact.html',context)
    

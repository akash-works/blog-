from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def contact(request):
    if request .method == "POST":
        name = request .POST.get("name")
        email = request .POST .get("email")
        phone = request .POST .get("phone")
        message = request .POST.get("message")
        a = User(name=name,email=email,phone=phone,message=message)
        a.save()

    return render(request,"contact.html")

def samp_post(request):
    return render(request,"post.html")
    
def aka(request):
    return HttpResponse("akash page")    
def sum (request):
    return HttpResponse(request ,"akash sen")    

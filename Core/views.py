from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")

def login(request):
    return HttpResponse("This is login page")

def register(request):
    return HttpResponse("This is register page")


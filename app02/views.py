from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(request):
    return render(request,"login.html")
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def login(request):
    return HttpResponse("app01login")

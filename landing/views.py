from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Subscription

# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username");
        password = request.POST.get("password");
        
        try:
            User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return  redirect('/admin')
        else:
            messages.error(request, "user does not exist")
            
    if request.user.is_authenticated:
        return redirect('/admin')
    else:    
        return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html')
    
def subscribe(request):
    if request.method == "POST":
        print(request.POST)
        sub = Subscription(email=request.POST['email'])
        sub.save()
        return redirect('subscribed')
        
    return render(request, 'index.html')

def subscribed(request):
    return render(request, 'subscribed.html')
    
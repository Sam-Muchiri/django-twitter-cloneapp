from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.form import signupForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def signup(request):
    if request.method=='POST':
        signupform=signupForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request, 'account successfully created')
            return redirect('signin')
    else:
        signupform=signupForm()
    return render(request, 'blog/register.html',{"form":signupform})

def signin(request):
    if request.method=='POST':
        signinform=AuthenticationForm(data=request.POST)
        if signinform.is_valid():
            
            login(request, signinform.get_user())
            messages.success(request, 'you successfully logged in')
            return redirect('home')
            
    else:
        signinform=AuthenticationForm()
    return render(request, 'blog/login.html',{"form":signinform})

def signout(request):
    logout(request)
    messages.success(request, 'you successfully logged out')
    return redirect('home')
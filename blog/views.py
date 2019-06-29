from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def signup(request):
    if request.method == 'POST':
        if request.POST ['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
              user = User.objects.create_user(
              request.POST['username'], password = request.POST['password1'])
              auth.login (request,user)
            return redirect('home')
        else:
            return render (request, 'accounts/signup.html', {'eror': 'Passwords must match'})
    else:
        return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request, 'login.html', {'error':'username or password is incorrect.'})
    else:
        return render (request,'login.html')
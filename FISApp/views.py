from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from store.models import *

def check_admin(user):
   return user.is_superuser

@user_passes_test(check_admin)
def homeAdmin(request):
    return render(request, 'homeAdmin.html')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user1 = form.cleaned_data.get('username')
          #  physics = Customer(user=user2, name= '', email='user.email')
          #  physics.save()
            messages.success(request, "Account is created successfully for "+user1)
            return redirect('login')
    context = {'form': form }
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        # physics = Customer(user=username, name="", email=user.email)
        # physics.save()
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect.")
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def solarsystem(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'News.html')

def token_send(request):
    return render(request, 'send_token.html')

def success(request):
    return render(request, 'success.html')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from FISApp.models import Profile
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from store.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
import uuid

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')








def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


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
            try:
                email = request.POST.get('email')
                username = request.POST.get('username')
                user_obj = User(username = username , email = email)
                auth_token = str(uuid.uuid4())
                # profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token,)
                # profile_obj.save()
                send_mail_after_registration(email , auth_token)
            except:
                p = 5
            return redirect('/token')
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
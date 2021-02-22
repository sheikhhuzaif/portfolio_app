from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from portfolio.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from portfolio.mail import send_joining_mail


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            if User.objects.filter(username=username).first() is None:
                user = User(username=username, email=email)
                user.set_password(raw_password=password)
                user.save()
                send_joining_mail(email,username)
                messages.success(request, "Account successfully created for " + username)
                return redirect('login')
            else:
                messages.error(request, "Account already exists")
        context = {}
        return render(request, 'signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Invalid Credentials")

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def edit(request):
    print(request.POST)
    return render(request, 'edit.html',{'range':range(1)})


def about(request):
    return render(request, 'about.html')

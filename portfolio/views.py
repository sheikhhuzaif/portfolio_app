from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.urls import reverse

from portfolio.forms import UserRegistrationForm
from portfolio.models.base import UserProfile


def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'signup.html',context)


def test(request):
    return render(request, 'index.html')

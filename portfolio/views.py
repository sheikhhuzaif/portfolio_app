from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from portfolio.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from portfolio.mail import send_joining_mail
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


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
                send_joining_mail(email, username)
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
    return render(request, 'edit.html', {'range': range(1)})


def display(request, username):
    try:
        user = User.objects.get(username=username)
        context = {
            'user': user
        }
        return render(request, 'view.html', context)
    except:
        return render(request, 'error.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def settings(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            old=request.POST.get('old')
            new=request.POST.get('new')
            username=request.user
            user=authenticate(request,username=username,password=old)
            if user is not None:
                user.set_password(new)
                user.save()
                user=authenticate(request,username=username,password=new)
                login(request,user)
                messages.info(request,'password change succesfully')
                return redirect('home')
            else:
                messages.info(request,'old password is wrong')

    return render(request,'settings.html')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            emailid = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=emailid))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    context = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, context)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html",
                  context={"password_reset_form": password_reset_form})

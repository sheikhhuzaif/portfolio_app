from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from portfolio.tasks import send_joining_mail,send_email
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
from portfolios.settings import EMAIL_HOST_USER

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            if (User.objects.filter(username=username).first() or User.objects.filter(email=email).first())is None:
                user = User(username=username, email=email)
                user.set_password(raw_password=password)
                user.save()
                send_joining_mail.delay(email, username)
                messages.success(request, "Account successfully created for " + username)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home')
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
    if request.method=='POST':
        data=request.POST
        fname=data.get('Fname')
        lname=data.get('Lname')
        user=User.objects.get(username=request.user)
        user.first_name=fname
        user.last_name=lname
        user.save()
        

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
    return render(request, 'settings.html')


@login_required(login_url='login')
def password_change(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            old = request.POST.get('old')
            new = request.POST.get('new')
            username = request.user
            user = authenticate(request, username=username, password=old)
            if user is not None:
                user.set_password(new)
                user.save()
                user = authenticate(request, username=username, password=new)
                login(request, user)
                messages.info(request, 'password change succesfully')
                return redirect('home')
            else:
                messages.info(request, 'old password is wrong')

    return render(request, 'password_settings.html')


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
                        'site_name': 'PortFolios',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, context)
                    try:
                        send_email.delay(subject, email, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request, "password_reset.html", {"password_reset_form": password_reset_form})


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject="Message from "+name+"("+email+")"
        
        if send_email.delay(subject,message,['sheikhhuzaif007@gmail.com']):
            return render(request,'contactsuccess.html')
        else:
            return render(request,'contactfail.html')

    return render(request,'contact.html')
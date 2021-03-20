from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from portfolio.tasks import send_joining_mail, send_email
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
from portfolio.models.base import *
import json
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator, NumericPasswordValidator
from django.core.exceptions import ValidationError


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        validators = [MinimumLengthValidator,
                  CommonPasswordValidator, NumericPasswordValidator]
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            if (User.objects.filter(username=username).first() or User.objects.filter(email=email).first()) is None:
                user = User(username=username, email=email)
                try:
                    for v in validators:
                        v().validate(password)
                except ValidationError as e:
                    messages.error(request, str(e))
                    return redirect('register')
                user.set_password(raw_password=password)
                user.save()
                # send_joining_mail.delay(email, username)
                messages.success(
                    request, "Account successfully created for " + username)
                user = authenticate(
                    request, username=username, password=password)
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Account already exists")
                return redirect('register')
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
    if request.method == 'POST':
        template = request.POST.get('template')
        print(request.POST.get('template'))
        user = User.objects.get_or_create(username=request.user)[0]
        userInfo = UserInfo.objects.get_or_create(user=user)[0]
        userInfo.view = template
        userInfo.save()
        return redirect('/view/'+str(request.user))
    return render(request, 'index.html')


@login_required(login_url='login')
def edit(request):
    if request.method == 'POST':
        data = request.POST
        fname = data.get('Fname')
        lname = data.get('Lname')
        user = User.objects.get_or_create(username=request.user)[0]
        user.first_name = fname
        user.last_name = lname
        user.save()
        userInfo = UserInfo.objects.get_or_create(user=user)[0]
        userInfo.phone = data.get('phone')
        userInfo.address = data.get('address')
        userInfo.about = data.get('about')
        try:
            picture = request.FILES['picture']

            userInfo.picture = picture

        except Exception as e:
            print(e)
        try:

            resume = request.FILES['resume']

            userInfo.resume = resume
        except Exception as e:
            print(e)
        userInfo.gender = data.get('gender')
        userInfo.profession = data.get('profession')
        userInfo.dob = data.get('dob')
        userInfo.save()
        i = 1
        while(data.get('degreename'+str(i))):
            Education(course_name=data.get('degreename'+str(i)), end_time=data.get('degreedate'+str(i)),
                      university=data.get('degreefrom'+str(i)), user=userInfo, gpa=data.get('degreegpa'+str(i))).save()
            i += 1
        i = 1
        while(data.get('skillname'+str(i))):
            Skills(name=data.get('skillname'+str(i)), user=userInfo).save()
            i += 1
        i = 1
        while(data.get('socialname'+str(i))):
            Social(username=data.get('socialname'+str(i)),
                   stype=data.get('socialtype'+str(i)), user=userInfo).save()
            i += 1
        i = 1
        while(data.get('jobtitle'+str(i))):
            Work(user=userInfo, title=data.get('jobtitle'+str(i)), start_date=data.get('startdate'+str(i)),
                 end_date=data.get('enddate'+str(i)), company=data.get('companyname'+str(i))).save()
            i += 1
        i = 1
        return redirect('home')
    if UserInfo.objects.filter(user=User.objects.get(username=request.user)).count():
        context = {
            'user': User.objects.get(username=request.user),
            'userInfo': UserInfo.objects.get(user=User.objects.get(username=request.user)),
            'number': Education.objects.filter(user=UserInfo.objects.get(user=User.objects.get(username=request.user))).count(),
            'education': list(Education.objects.filter(user=UserInfo.objects.get(user=User.objects.get(username=request.user)))),
            'skills': list(Skills.objects.filter(user=UserInfo.objects.get(user=User.objects.get(username=request.user)))),
            'socials': list(Social.objects.filter(user=UserInfo.objects.get(user=User.objects.get(username=request.user)))),
            'work': list(Work.objects.filter(user=UserInfo.objects.get(user=User.objects.get(username=request.user))))
        }
    else:
        context = {}
    return render(request, 'edit.html', context)


def templatechooser(template):
    switcher = {
        0: "view.html",
        1: "view1.html",
        2: "view2.html",
        3: "view3.html",
    }

    return switcher.get(template)


def display(request, username):
    try:
        user = User.objects.get(username=username)
        userInfo = UserInfo.objects.get(user=user)
        template = templatechooser(userInfo.view)
        education = list(Education.objects.filter(user=userInfo))
        skills = list(Skills.objects.filter(user=userInfo))
        work = list(Work.objects.filter(user=userInfo))
        social = list(Social.objects.filter(user__user__username=username))
        context = {
            'user': user,
            'userInfo': userInfo,
            'education': education,
            'skills': skills,
            'work': work,
            'social': social
        }
        if request.method == 'POST':
            sender_name = request.POST.get('name')
            sender_email = request.POST.get('email')
            sender_subject = request.POST.get('subject')
            sender_mail = request.POST.get('message')
            try:
                send_email.delay(subject='Message from '+sender_name+'('+sender_email+')',
                                 message=sender_mail, recipient_list=[user.email, ])
                messages.info(
                    request, "I will get back to you as soon as possible")
            except Exception:
                messages.error(request, "Could not contact. Try Again Later")
        return render(request, template, context)
    except Exception as e:
        print(e)
        return render(request, 'error.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def settings(request):
    return render(request, 'settings.html')


@login_required(login_url='login')
def password_change(request):
    validators = [MinimumLengthValidator,
                  CommonPasswordValidator, NumericPasswordValidator]
    if request.method == 'POST':
        if request.user.is_authenticated:
            old = request.POST.get('old')
            new = request.POST.get('new')
            try:
                for v in validators:
                    v().validate(new)
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('password')
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
                        send_email.delay(subject, email, [user.email])
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
            else:
                messages.info(request, "Account not registered with us")
    password_reset_form = PasswordResetForm()
    return render(request, "password_reset.html", {"password_reset_form": password_reset_form})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = str(request.POST.get('subject'))+" " + \
            str(request.POST.get('message'))
        subject = "Message from "+name+"("+email+")"

        if send_email.delay(subject, message, ['sheikhhuzaif007@gmail.com']):
            return render(request, 'contactsuccess.html')
        else:
            return render(request, 'contactfail.html')

    return render(request, 'contact.html')

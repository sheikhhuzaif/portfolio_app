from django.conf import settings
from django.core.mail import send_mail


def send_joining_mail(email, username):
    subject = 'Welcome Aboard'
    message = f'Hi {username}, thank you for registering with portfolios'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)

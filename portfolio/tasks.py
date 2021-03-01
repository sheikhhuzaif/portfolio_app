from django.conf import settings
from django.core.mail import send_mail
from portfolio.celery import app
import logging


logger=logging.getLogger(__name__)


@app.task
def send_joining_mail(email, username):
    subject = 'Welcome Aboard'
    message = f'Hi {username}, thank you for registering with portfolios'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        logger.error(e)

@app.task
def send_email(subject,message,recipient_list):
    try:
        send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)
    except Exception as e:
        logger.error(e)


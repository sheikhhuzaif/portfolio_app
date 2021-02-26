from django.contrib.auth.models import User
from django.db import models
from .utils import GENDER_CHOICES, SOCIAL_CHOICES


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intro = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=20,blank=True, null=True, choices=GENDER_CHOICES)
    picture = models.ImageField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)


class Skills(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Education(models.Model):
    course_name = models.CharField(max_length=128, blank=False)
    start_time = models.DateField()
    end_time = models.DateField()
    gpa = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Work(models.Model):
    title = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=128)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.company


class Social(models.Model):
    type = models.CharField(max_length=20,choices=SOCIAL_CHOICES)
    username = models.CharField(max_length=128)
    link = models.URLField()

    def __str__(self):
        return self.type + self.username

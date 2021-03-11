from django.contrib.auth.models import User
from django.db import models
from .utils import GENDER_CHOICES, SOCIAL_CHOICES
import datetime


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True, null=True)
    phone = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=20,blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    view=models.IntegerField(blank=False,null=False, default=0)
    profession=models.CharField(max_length=40)
    dob=models.DateField()

    @property
    def age(self):
        return datetime.date.today().year - self.dob.year - ((datetime.date.today().month, datetime.date.today().day) < (self.dob.month, self.dob.day))


class Skills(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Education(models.Model):
    course_name = models.CharField(max_length=128, blank=False)
    university=models.CharField(max_length=128,blank=False,null=True)
    end_time = models.IntegerField()
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
    stype = models.CharField(max_length=20,default="Social Media")
    username = models.CharField(max_length=128)
    user=models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    @property
    def link1(self):
        return str(self.stype)+".com/"+str(self.username) 


    @property
    def get_type(self):
        return str(self.stype).lower()

    def __str__(self):
        return self.type + self.username

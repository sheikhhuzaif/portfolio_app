# Generated by Django 3.1.6 on 2021-03-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_userinfo_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='profession',
        ),
    ]

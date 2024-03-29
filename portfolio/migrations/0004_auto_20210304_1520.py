# Generated by Django 3.1.6 on 2021-03-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210302_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='start_time',
        ),
        migrations.AddField(
            model_name='education',
            name='university',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_time',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

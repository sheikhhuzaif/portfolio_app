# Generated by Django 3.1.6 on 2021-03-07 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210307_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.userinfo'),
        ),
    ]

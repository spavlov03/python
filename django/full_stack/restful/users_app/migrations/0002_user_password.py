# Generated by Django 2.2.4 on 2023-03-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123456789', max_length=100),
        ),
    ]

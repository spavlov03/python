# Generated by Django 2.2.4 on 2023-02-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

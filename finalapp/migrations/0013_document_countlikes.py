# Generated by Django 2.1.2 on 2018-12-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0012_likeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='countlikes',
            field=models.IntegerField(default='0'),
        ),
    ]
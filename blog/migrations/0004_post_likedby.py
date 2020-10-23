# Generated by Django 2.2 on 2020-10-02 18:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likedby',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]

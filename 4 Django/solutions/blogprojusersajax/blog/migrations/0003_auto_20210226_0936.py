# Generated by Django 3.1.4 on 2021-02-26 17:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210226_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorited_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

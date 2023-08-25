# Generated by Django 4.2.3 on 2023-08-24 16:37

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogPosts', '0003_rename_category_post_category_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 24, 16, 37, 33, 63094, tzinfo=datetime.timezone.utc)),
        ),
    ]
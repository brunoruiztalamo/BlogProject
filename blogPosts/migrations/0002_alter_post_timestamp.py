# Generated by Django 4.2.3 on 2023-08-19 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 21, 37, 27, 377729, tzinfo=datetime.timezone.utc)),
        ),
    ]
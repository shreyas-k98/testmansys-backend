# Generated by Django 4.1.2 on 2022-10-25 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_test_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.TimeField(default=datetime.datetime(2022, 10, 25, 10, 23, 7, 811856, tzinfo=datetime.timezone.utc)),
        ),
    ]
# Generated by Django 3.2.9 on 2022-01-05 11:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0010_auto_20220104_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliances',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 11, 3, 47, 553654, tzinfo=utc)),
        ),
    ]
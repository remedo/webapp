# Generated by Django 2.2.1 on 2019-06-20 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='timestamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 6, 20, 9, 55, 30, 164579, tzinfo=utc)),
        ),
    ]
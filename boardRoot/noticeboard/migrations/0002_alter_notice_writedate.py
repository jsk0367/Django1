# Generated by Django 3.2 on 2021-09-09 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='writeDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 1, 44, 12, 337943), editable=False),
        ),
    ]
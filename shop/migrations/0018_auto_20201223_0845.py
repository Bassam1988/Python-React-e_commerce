# Generated by Django 3.1.1 on 2020-12-23 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20201223_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='viewd_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20201220_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.FloatField(),
        ),
    ]
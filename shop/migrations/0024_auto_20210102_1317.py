# Generated by Django 3.1.1 on 2021-01-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20201231_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/subCategories/2021-01-02 13:17:34.302574'),
        ),
    ]
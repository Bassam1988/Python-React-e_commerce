# Generated by Django 3.1.7 on 2021-04-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20210402_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/subCategories/2021-04-02 09:40:01.598052'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/subCategories/2021-04-02 09:40:01.604010'),
        ),
    ]

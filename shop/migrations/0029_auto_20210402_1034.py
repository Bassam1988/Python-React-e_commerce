# Generated by Django 3.1.7 on 2021-04-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20210402_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/subCategories/2021-04-02 10:34:54.112834'),
        ),
        migrations.AlterField(
            model_name='product',
            name='s_categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='shop.SubCategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/subCategories/2021-04-02 10:34:54.113942'),
        ),
    ]

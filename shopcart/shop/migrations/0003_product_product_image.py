# Generated by Django 3.1.7 on 2021-05-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

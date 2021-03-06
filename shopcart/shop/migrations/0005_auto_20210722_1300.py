# Generated by Django 2.2.13 on 2021-07-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=None),
        ),
    ]

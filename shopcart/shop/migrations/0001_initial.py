# Generated by Django 3.1.7 on 2021-05-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Product_name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=400)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]

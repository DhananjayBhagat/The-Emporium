# Generated by Django 4.2.2 on 2023-08-03 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20190620_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
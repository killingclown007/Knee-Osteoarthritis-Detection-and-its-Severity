# Generated by Django 3.0.3 on 2021-02-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kneearth', '0012_user_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='CreditCard',
            field=models.CharField(default=None, max_length=16),
        ),
        migrations.AddField(
            model_name='user_details',
            name='Cvv',
            field=models.CharField(default=None, max_length=3),
        ),
        migrations.AddField(
            model_name='user_details',
            name='Expiry',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
# Generated by Django 3.0.3 on 2021-02-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kneearth', '0009_chat_details_msgfrom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_details',
            name='Datetime',
            field=models.DateTimeField(),
        ),
    ]

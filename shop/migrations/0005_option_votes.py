# Generated by Django 5.0 on 2024-01-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

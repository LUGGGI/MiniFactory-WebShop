# Generated by Django 5.0 on 2024-01-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_order_products_order_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.JSONField(default=None),
        ),
    ]

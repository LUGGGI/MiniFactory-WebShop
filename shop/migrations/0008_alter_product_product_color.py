# Generated by Django 5.0 on 2024-01-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_option_text_option_display_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_color',
            field=models.CharField(choices=[('WHITE', 'White'), ('RED', 'Red'), ('BLUE', 'Blue')], max_length=5),
        ),
    ]

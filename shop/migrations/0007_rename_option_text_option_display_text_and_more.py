# Generated by Django 5.0 on 2024-01-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_votes_option_selections'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='option_text',
            new_name='display_text',
        ),
        migrations.RemoveField(
            model_name='option',
            name='product',
        ),
        migrations.RemoveField(
            model_name='option',
            name='selections',
        ),
        migrations.AddField(
            model_name='option',
            name='name_int',
            field=models.CharField(default='INT', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='option',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(to='shop.option'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_color',
            field=models.CharField(choices=[('White', 'WHITE'), ('Red', 'RED'), ('Blue', 'BLUE')], max_length=5),
        ),
    ]

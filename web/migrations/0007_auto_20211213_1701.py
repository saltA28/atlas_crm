# Generated by Django 2.2.1 on 2021-12-13 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_product_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='addr',
            new_name='company',
        ),
    ]
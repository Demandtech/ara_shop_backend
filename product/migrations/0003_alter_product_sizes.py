# Generated by Django 4.2.4 on 2023-08-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.JSONField(),
        ),
    ]
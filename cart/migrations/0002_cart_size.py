# Generated by Django 4.2.4 on 2023-08-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default='Medium', max_length=15),
            preserve_default=False,
        ),
    ]
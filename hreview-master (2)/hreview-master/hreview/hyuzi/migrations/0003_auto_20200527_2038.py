# Generated by Django 3.0.6 on 2020-05-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyuzi', '0002_auto_20200527_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]

# Generated by Django 3.0 on 2021-03-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210309_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Expiry_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Manufacturing_date',
            field=models.DateField(blank=True),
        ),
    ]

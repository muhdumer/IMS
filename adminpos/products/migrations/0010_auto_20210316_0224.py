# Generated by Django 3.0 on 2021-03-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210314_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Manufacturing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

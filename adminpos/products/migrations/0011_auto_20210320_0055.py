# Generated by Django 3.1.7 on 2021-03-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210316_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Purchase_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='product',
            name='Selling_price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpurchasedetail',
            name='Price',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='SubTotal',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20210320_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='Tax',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=19),
        ),
    ]

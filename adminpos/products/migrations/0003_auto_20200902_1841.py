# Generated by Django 3.0.6 on 2020-09-02 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200902_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_Brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_brand', to='products.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_cat', to='products.Category'),
        ),
    ]

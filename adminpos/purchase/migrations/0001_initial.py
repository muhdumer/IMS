# Generated by Django 3.0.6 on 2020-10-02 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_auto_20201002_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPurchaseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_code', models.CharField(default='', max_length=50)),
                ('product_desc', models.TextField(blank=True)),
                ('Price', models.PositiveIntegerField()),
                ('PurchaseQuantity', models.PositiveIntegerField()),
                ('Discount', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoiceno', models.CharField(max_length=50, unique=True)),
                ('Suppliername', models.CharField(max_length=250)),
                ('Invoicedate', models.DateField()),
                ('SupplierEmail', models.EmailField(blank=True, max_length=254)),
                ('Contactno', models.CharField(blank=True, max_length=12)),
                ('Address', models.TextField(blank=True)),
                ('Invoicetype', models.CharField(max_length=50)),
                ('SubTotal', models.PositiveIntegerField()),
                ('Discount', models.PositiveIntegerField(blank=True, default=0)),
                ('Tax', models.PositiveIntegerField(blank=True, default=0)),
                ('Shippingcharge', models.PositiveIntegerField(blank=True, default=0)),
                ('Products', models.ManyToManyField(through='purchase.ProductPurchaseDetail', to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='productpurchasedetail',
            name='Invoiceno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productdetail', to='purchase.PurchaseInvoice'),
        ),
        migrations.AddField(
            model_name='productpurchasedetail',
            name='Pcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
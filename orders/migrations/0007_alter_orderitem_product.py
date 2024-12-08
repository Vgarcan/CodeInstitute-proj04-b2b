# Generated by Django 5.1.1 on 2024-12-08 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_shipaddr_address_alter_shipaddr_city_and_more'),
        ('products', '0008_orderproductsnapshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.orderproductsnapshot'),
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-04 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('payments', '0001_initial'),
        ('products', '0003_auto_20211204_0703'),
        ('baskets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line_1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('line_2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone Number')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('postcode', models.CharField(max_length=10, verbose_name='Post Code')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Billing Address',
                'verbose_name_plural': 'Billing Addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('status', models.CharField(choices=[('PW', 'Payment Waiting'), ('CO', 'Completed'), ('CA', 'Canceled')], default='PW', max_length=2)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Order Price')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baskets.basket', verbose_name='Basket')),
                ('billing_address', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='billing_address_orders', to='orders.billingaddress', verbose_name='Billing Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('shipping_address', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='shipping_address_orders', to='orders.billingaddress', verbose_name='Shipping Address')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line_1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('line_2', models.CharField(max_length=255, verbose_name='Address Line 2')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone Number')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('postcode', models.CharField(max_length=10, verbose_name='Post Code')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Shipping Address',
                'verbose_name_plural': 'Shipping Addresses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order Item Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='OrderBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Bank Account Name')),
                ('iban', models.CharField(max_length=255, verbose_name='IBAN Number')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.bank', verbose_name='Bank Name')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order Bank Account',
                'verbose_name_plural': 'Order Bank Accounts',
            },
        ),
    ]

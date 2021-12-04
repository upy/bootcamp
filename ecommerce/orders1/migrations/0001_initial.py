from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baskets', '0001_initial'),
        ('products', '0003_auto_20211201_1646'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line_1', models.CharField(max_length=255, verbose_name='Line 1')),
                ('line_2', models.CharField(max_length=255, verbose_name='Line 2')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('district', models.CharField(max_length=20, verbose_name='District')),
                ('postcode', models.CharField(max_length=10, verbose_name='Postcode')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'billing adress',
                'verbose_name_plural': 'billing addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Price')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baskets.basket', verbose_name='Basket')),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.billingaddress', verbose_name='Billing Address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'verbose_name': 'shipping adress',
                'verbose_name_plural': 'shipping addresses',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line_1', models.CharField(max_length=255, verbose_name='Line 1')),
                ('line_2', models.CharField(max_length=255, verbose_name='Line 2')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('district', models.CharField(max_length=20, verbose_name='District')),
                ('postcode', models.CharField(max_length=10, verbose_name='Postcode')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'shipping adress',
                'verbose_name_plural': 'shipping addresses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order', verbose_name='Order')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.price', verbose_name='Price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
            },
        ),
        migrations.CreateModel(
            name='OrderBankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('iban', models.CharField(max_length=50, verbose_name='IBAN')),
                ('bank_name', models.CharField(max_length=30, verbose_name='Bank Name')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'order bank account',
                'verbose_name_plural': 'order bank accounts',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.shippingaddress', verbose_name='Shipping Address'),
        ),
    ]
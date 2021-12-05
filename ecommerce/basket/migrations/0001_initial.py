# Generated by Django 3.2.9 on 2021-12-05 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20211205_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('status', models.CharField(choices=[('open', 'Open'), ('submitted', 'Submitted'), ('merged', 'Merged')], max_length=20, verbose_name='Status')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'basket',
                'verbose_name_plural': 'baskets',
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'basketItem',
                'verbose_name_plural': 'basketItems',
            },
        ),
    ]

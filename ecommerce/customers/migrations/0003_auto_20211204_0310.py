# Generated by Django 3.2.9 on 2021-12-04 00:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('customers', '0002_address_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed.", regex='^[0-9]+$')], verbose_name='Postal Code'),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]

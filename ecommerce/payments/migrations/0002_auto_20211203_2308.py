# Generated by Django 3.2.9 on 2021-12-03 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': 'bank', 'verbose_name_plural': 'banks'},
        ),
        migrations.AlterModelOptions(
            name='bankaccount',
            options={'verbose_name': 'bank account', 'verbose_name_plural': 'bank accounts'},
        ),
    ]

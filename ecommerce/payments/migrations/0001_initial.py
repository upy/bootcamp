# Generated by Django 3.2.9 on 2021-12-02 19:48

from django.db import migrations, models
import django.db.models.deletion
import django_iban.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'bank',
                'verbose_name_plural': 'banks',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('iban', django_iban.fields.IBANField(max_length=34)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.bank', verbose_name='Bank')),
            ],
            options={
                'verbose_name': 'Bank Accounts',
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
    ]

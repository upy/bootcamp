# Generated by Django 3.2.9 on 2021-12-03 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basketitem',
            options={'verbose_name': 'basket item', 'verbose_name_plural': 'basket items'},
        ),
    ]

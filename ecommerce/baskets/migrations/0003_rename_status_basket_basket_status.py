# Generated by Django 3.2.9 on 2021-12-05 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0002_auto_20211203_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='status',
            new_name='basket_status',
        ),
    ]

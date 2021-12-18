# Generated by Django 3.2.9 on 2021-12-14 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baskets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
    ]

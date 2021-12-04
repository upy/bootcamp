from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_price_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.Category', verbose_name='Category'),
        ),
    ]
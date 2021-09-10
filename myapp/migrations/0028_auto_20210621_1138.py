# Generated by Django 3.2.1 on 2021-06-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20210621_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_items',
            name='cart',
        ),
        migrations.AddField(
            model_name='order_items',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_items',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order_items',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
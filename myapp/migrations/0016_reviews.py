# Generated by Django 3.2.1 on 2021-06-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210604_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=255)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.products')),
            ],
        ),
    ]
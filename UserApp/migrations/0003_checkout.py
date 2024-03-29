# Generated by Django 5.0 on 2024-01-31 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(default='', max_length=15)),
                ('country', models.CharField(max_length=25)),
                ('zip', models.CharField(max_length=15)),
                ('cartid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.cart')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.login')),
            ],
        ),
    ]

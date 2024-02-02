# Generated by Django 5.0 on 2024-01-25 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_addmov_price'),
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.addmov')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.login')),
            ],
        ),
    ]
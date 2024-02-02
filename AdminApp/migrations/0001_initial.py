# Generated by Django 5.0 on 2024-01-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=20)),
                ('catdescription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AddMov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=20)),
                ('moviecategory', models.CharField(max_length=20)),
                ('movielang', models.CharField(max_length=20)),
                ('moviegenre', models.CharField(max_length=20)),
                ('image', models.ImageField(default='null.jpg', upload_to='photos')),
            ],
        ),
    ]
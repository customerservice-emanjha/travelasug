# Generated by Django 2.2.4 on 2020-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_park_hotel_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park_hotel_city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(default='none', max_length=1000)),
                ('h_img', models.CharField(default='none', max_length=500)),
                ('cat', models.CharField(default='none', max_length=200)),
                ('city', models.CharField(default='none', max_length=200)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2020-09-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_twitter_twit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park_hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('park_json', models.CharField(default='none', max_length=30000)),
            ],
        ),
        migrations.DeleteModel(
            name='UserLocation',
        ),
    ]
# Generated by Django 2.2.4 on 2020-09-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200902_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter',
            name='twit_date',
            field=models.CharField(default='02-09-2020', max_length=100),
        ),
    ]

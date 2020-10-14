# Generated by Django 2.2.4 on 2020-04-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanjha_admin', '0006_usa_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Virtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(default='empty', max_length=2000)),
                ('image', models.FileField(default='', upload_to='activities')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
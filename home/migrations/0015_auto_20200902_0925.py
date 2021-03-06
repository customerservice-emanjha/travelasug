# Generated by Django 2.2.4 on 2020-09-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200901_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter',
            name='twit_json',
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_count',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_id',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_img',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_like',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_text',
            field=models.CharField(default='none', max_length=2500),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_user1',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='twitter',
            name='twit_user2',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='dt',
            field=models.CharField(default='none', max_length=50),
        ),
    ]

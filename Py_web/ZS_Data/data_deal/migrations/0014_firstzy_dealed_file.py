# Generated by Django 3.1.1 on 2020-09-13 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0013_auto_20200913_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstzy',
            name='Dealed_File',
            field=models.FilePathField(default=1, path='File/FirstZY/result'),
            preserve_default=False,
        ),
    ]

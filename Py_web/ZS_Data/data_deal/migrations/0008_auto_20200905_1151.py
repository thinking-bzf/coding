# Generated by Django 3.1 on 2020-09-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0007_auto_20200905_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstzy',
            name='File',
            field=models.FileField(upload_to='File/FirstZY/original/'),
        ),
        migrations.AlterField(
            model_name='original_file',
            name='File',
            field=models.FileField(upload_to='File/original/'),
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-13 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0016_auto_20200913_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='original_file',
            name='cleaned_file',
        ),
    ]
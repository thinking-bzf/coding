# Generated by Django 3.1 on 2020-09-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0010_auto_20200906_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='original_file',
            name='clean_message',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
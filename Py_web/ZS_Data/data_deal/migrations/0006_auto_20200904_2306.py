# Generated by Django 3.1 on 2020-09-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0005_auto_20200904_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='original_file',
            name='File',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='original_file',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

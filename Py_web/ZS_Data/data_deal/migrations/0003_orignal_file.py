# Generated by Django 3.1 on 2020-08-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0002_auto_20200831_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='orignal_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='File/orignal')),
                ('file_name', models.CharField(max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

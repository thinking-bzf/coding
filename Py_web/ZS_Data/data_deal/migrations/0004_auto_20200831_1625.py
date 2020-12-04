# Generated by Django 3.1 on 2020-08-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0003_orignal_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='original_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='File/original')),
                ('file_name', models.CharField(max_length=50)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='orignal_file',
        ),
    ]
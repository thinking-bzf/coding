# Generated by Django 3.1.1 on 2020-09-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_deal', '0014_firstzy_dealed_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='original_file',
            name='cleaned_FilePath',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='original_file',
            name='cleaned_file',
            field=models.FilePathField(path='File\\data_clean'),
        ),
    ]

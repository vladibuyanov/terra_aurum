# Generated by Django 4.1.5 on 2024-02-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_filemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='file_name',
            field=models.CharField(default='qwerty', max_length=200),
            preserve_default=False,
        ),
    ]
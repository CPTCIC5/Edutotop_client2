# Generated by Django 3.2 on 2021-08-21 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210821_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='file',
            field=models.FileField(default='default.pdf', upload_to='Notes'),
        ),
    ]

# Generated by Django 3.2 on 2021-08-21 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name_plural': 'Notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='file',
            field=models.FileField(default='default.pdf', upload_to=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

# Generated by Django 3.2 on 2021-09-06 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_notes_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='file',
            field=models.FileField(upload_to='Notes', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]

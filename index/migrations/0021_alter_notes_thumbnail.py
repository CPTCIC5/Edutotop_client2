# Generated by Django 3.2 on 2021-10-13 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_alter_video_vid_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default_notes.jpeg', upload_to='thumbnail_notes', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
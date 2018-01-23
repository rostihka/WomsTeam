# Generated by Django 2.0.1 on 2018-01-23 10:49

import client.validators.image_dimensions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='client/', validators=[client.validators.image_dimensions.ImageDimensions(200, 200)], verbose_name='Аватар'),
        ),
    ]

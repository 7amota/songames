# Generated by Django 4.2.1 on 2023-06-21 02:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_character_age_character_birthday_character_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='details',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(100), django.core.validators.MaxLengthValidator(150)]),
        ),
    ]
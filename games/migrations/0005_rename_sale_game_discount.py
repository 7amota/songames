# Generated by Django 4.2.1 on 2023-06-18 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_rename_bannerlogo_game_bannerlogo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='sale',
            new_name='discount',
        ),
    ]

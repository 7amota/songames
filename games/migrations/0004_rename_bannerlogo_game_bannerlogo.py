# Generated by Django 4.2.1 on 2023-06-18 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='BannerLogo',
            new_name='bannerLogo',
        ),
    ]
# Generated by Django 4.2.1 on 2023-06-18 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_game_status_alter_game_trend_alter_game_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Game',
        ),
        migrations.RemoveField(
            model_name='character',
            name='game',
        ),
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='games.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='character',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='games.character'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-04 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='character',
            new_name='category',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0008_fill_slug_for_existing_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]

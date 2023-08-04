# Generated by Django 4.2.2 on 2023-06-22 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0004_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='models_app.university'),
            preserve_default=False,
        ),
    ]
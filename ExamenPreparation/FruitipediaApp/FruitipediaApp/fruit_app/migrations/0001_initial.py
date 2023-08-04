# Generated by Django 4.2.3 on 2023-07-22 09:46

import FruitipediaApp.fruit_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), FruitipediaApp.fruit_app.models.all_letter_validator])),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), FruitipediaApp.fruit_app.models.first_letter_validator])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(2), FruitipediaApp.fruit_app.models.first_letter_validator])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
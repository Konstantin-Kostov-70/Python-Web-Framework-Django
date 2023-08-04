# Generated by Django 4.2.3 on 2023-07-14 22:44

import MyPlantApp.plant_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinValueValidator(2), MyPlantApp.plant_app.models.is_letter])),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantApp.plant_app.models.is_upper])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantApp.plant_app.models.is_upper])),
                ('profile_picture', models.URLField()),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('years', models.IntegerField()),
                ('biography', models.TextField()),
                ('course_create_on', models.DateTimeField(auto_now_add=True)),
                ('course_update_on', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

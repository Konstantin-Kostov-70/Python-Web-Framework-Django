# Generated by Django 4.2.2 on 2023-06-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0005_student_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=25),
        ),
    ]

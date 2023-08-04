from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def is_upper(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def is_letter(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2),
        )
    )
    first_name = models.CharField(
        max_length=20,
        validators=(
            is_upper,
        )
    )
    last_name = models.CharField(
        max_length=20,
        validators=(
            is_upper,
        )
    )
    profile_picture = models.URLField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class PlantModel(models.Model):
    type = models.CharField(
        max_length=14,
        choices=(
            ("Outdoor Plants", "Outdoor Plants"),
            ("Indoor Plants", "Indoor Plants"),
        )
    )
    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
            is_letter,
        )
    )
    image = models.URLField()
    description = models.TextField()
    price = models.FloatField()

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


def min_len_validators(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def correct_year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
           min_len_validators,
        )
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(18),
        )
    )
    password = models.CharField(
        max_length=30
    )
    first_name = models.CharField(
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        blank=True
    )
    picture = models.URLField(
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CarModel(models.Model):
    type = models.CharField(
        max_length=10,
        choices=(
            ("Sports Car", "Sports Car"),
            ("Pickup", "Pickup"),
            ("Crossover", "Crossover"),
            ("Minibus", "Minibus"),
            ("Other", "Other")
        )
    )
    model = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
        )
    )
    year = models.IntegerField(
        validators=(
            correct_year_validator,
        )
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(1),
        )
    )




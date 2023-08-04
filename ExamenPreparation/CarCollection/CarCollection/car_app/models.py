from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(2, message="The username must be a minimum of 2 chars"),
        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=(
            MinValueValidator(18),
        )
    )
    password = models.CharField(
        max_length=30
    )
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    image = models.URLField()

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=(
            ("Sports Car", "Sports Car"),
            ("Pickup", "Pickup"),
            ("Crossover", "Crossover"),
            ("Minibus", "Minibus"),
            ("Other", "Other"),
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
            year_validator,
        )
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(1),
        )
    )




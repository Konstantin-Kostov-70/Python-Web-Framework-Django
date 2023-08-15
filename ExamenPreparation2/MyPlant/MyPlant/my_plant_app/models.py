from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def is_capital_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


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
            is_capital_validator,
        )
    )
    last_name = models.CharField(
        max_length=20,
        validators=(
            is_capital_validator,
        )
    )
    picture = models.URLField(
        blank=True
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PlantModel(models.Model):
    type = models.CharField(
        max_length=14,
        choices=(
            ("Outdoor Plants", "Outdoor Plants"),
            ("Indoor Plants", "Indoor Plants")
        )
    )
    name = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(2),
        )
    )
    image = models.URLField()

    text = models.TextField()

    price = models.FloatField()

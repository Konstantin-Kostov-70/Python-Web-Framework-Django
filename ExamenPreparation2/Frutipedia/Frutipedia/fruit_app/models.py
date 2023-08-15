from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters!")


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(2),
        )
    )
    last_name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(2),
        )
    )
    email = models.EmailField(
        max_length=40
    )
    password = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(8),
        )
    )
    image = models.URLField(
        blank=True
    )

    age = models.PositiveIntegerField(
        blank=True,
        default=18
    )


class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator
        )
    )
    image = models.URLField()

    description = models.TextField()
    nutrition = models.TextField(
        blank=True
    )

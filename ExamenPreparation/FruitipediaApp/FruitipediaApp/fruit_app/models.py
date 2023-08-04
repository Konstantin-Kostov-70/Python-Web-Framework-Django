from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator


def first_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def all_letter_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Fruit name should contain only letters !")


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(2),
            first_letter_validator
        )
    )

    last_name = models.CharField(
        max_length=35,
        validators=(
            MinLengthValidator(2),
            first_letter_validator
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
        null=True,
        blank=True
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class FruitModel(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            all_letter_validator
        )
    )

    image = models.URLField()
    description = models.TextField()
    nutrition = models.TextField()











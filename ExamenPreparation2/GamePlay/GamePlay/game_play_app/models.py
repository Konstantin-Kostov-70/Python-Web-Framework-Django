from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator


def rating_validator(value):
    if value < 0.1 or value > 5.0:
        raise ValidationError("Value must be between 0.1 and 5.0")


class ProfileModel(models.Model):
    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=(
            MinValueValidator(12),
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
    image = models.URLField(
        blank=True
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    title = models.CharField(
        max_length=30,
        unique=True
    )
    category = models.CharField(
        max_length=15,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other")
        )
    )
    rating = models.FloatField(
        validators=(
            rating_validator,
        )
    )
    max_level = models.PositiveIntegerField(
        validators=(
            MinValueValidator(1),
        )
    )
    image = models.URLField()
    summary = models.TextField()

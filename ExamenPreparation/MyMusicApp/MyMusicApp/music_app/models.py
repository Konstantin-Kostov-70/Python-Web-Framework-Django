from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


def username_validator(value):
    for ch in value:
        if not ch.isalnum() and not ch == "_":
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            username_validator
        )
    )
    email = models.EmailField()
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True
    )
    artist = models.CharField(
        max_length=30
    )
    genre = models.CharField(
        max_length=30,
        choices=(
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other")
        )
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )
    )

    def __str__(self):
        return self.album_name


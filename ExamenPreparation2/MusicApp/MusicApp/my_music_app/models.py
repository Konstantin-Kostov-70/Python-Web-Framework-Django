from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

"""
•	Album

o	Description
	Text field, optional.
o	Image URL
	URL field, required.
o	Price
	Float field, required.
	The number of decimal places of the price should not be specified in the database.
	The price cannot be below 0.0.


"""


def validate_username(value):
    if not value.isalnum() and "_" not in value:
        raise ValidationError('The username can only consist of letters, numbers, and underscores.')


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username
        )
    )
    email = models.EmailField()
    age = models.PositiveIntegerField()


class Album(models.Model):
    name = models.CharField(
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
            ("Other", "Other"),
        )
    )
    description = models.TextField(
        blank=True
    )
    image = models.URLField()
    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        )
    )

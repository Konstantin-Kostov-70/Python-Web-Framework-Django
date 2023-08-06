from django.db import models
from DynamicWebsite.cars.models import Car


class Order(models.Model):
    name = models.CharField(
        max_length=20
    )
    cars = models.ManyToManyField(
        Car,
    )
    total = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    total_price = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name



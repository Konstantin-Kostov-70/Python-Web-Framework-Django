from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

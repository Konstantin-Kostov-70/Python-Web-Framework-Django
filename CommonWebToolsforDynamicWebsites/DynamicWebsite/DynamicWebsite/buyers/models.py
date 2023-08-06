from django.contrib.auth.models import User
from django.db import models


class Buyer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    from_signal = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.user.username

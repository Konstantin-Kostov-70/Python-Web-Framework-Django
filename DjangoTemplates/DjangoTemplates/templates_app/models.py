from django.db import models


class Articles(models.Model):
    title = models.CharField(
        max_length=30
    )
    price = models.FloatField()

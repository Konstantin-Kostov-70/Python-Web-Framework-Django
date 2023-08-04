from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20
    )
    last_name = models.CharField(
        max_length=20
    )
    age = models.IntegerField()
    image = models.URLField()

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    title = models.CharField(
        max_length=30
    )
    image = models.URLField()
    content = models.TextField()
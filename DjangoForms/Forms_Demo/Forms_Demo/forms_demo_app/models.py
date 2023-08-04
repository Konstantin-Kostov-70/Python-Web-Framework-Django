from django.db import models


class University(models.Model):
    name = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(
        max_length=30
    )
    age = models.IntegerField()
    university = models.ManyToManyField(
        University,
    )

    def __str__(self):
        return self.name


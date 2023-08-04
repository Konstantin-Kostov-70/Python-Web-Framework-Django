from django.db import models


class Task(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )
    description = models.TextField()

    priority = models.IntegerField()

    def __str__(self):
        return f'task: {self.name}'

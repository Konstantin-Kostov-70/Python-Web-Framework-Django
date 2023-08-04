from django.db import models
from Forms_Part2.forms_app2.validators import validate_text, validate_priority


class Person(models.Model):
    name = models.CharField(
        max_length=30
    )
    profile_image = models.ImageField(
        upload_to='persons',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS_PER_PERSON = 3
    text = models.CharField(
        max_length=25,
        validators=(
            validate_text,
        )
    )
    priority = models.IntegerField(
       validators=(
           validate_priority,
       )
    )
    is_done = models.BooleanField(
        default=False
    )
    assignee = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

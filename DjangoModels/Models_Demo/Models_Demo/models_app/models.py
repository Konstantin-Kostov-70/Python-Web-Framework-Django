from django.db import models


class University(models.Model):
    name = models.CharField(
        max_length=15,
    )
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):

    class Meta:
        ordering = ('-age',)

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
    )

    age = models.IntegerField()

    biography = models.TextField()

    course_create_on = models.DateTimeField(
        auto_now_add=True
    )

    course_update_on = models.DateTimeField(
        auto_now=True
    )

    email = models.EmailField()

    level = models.CharField(
        max_length=25,
        choices=[
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
            ('Senior', 'Senior'),
        ]
    )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'id:{self.id} Name: {self.fullname}'



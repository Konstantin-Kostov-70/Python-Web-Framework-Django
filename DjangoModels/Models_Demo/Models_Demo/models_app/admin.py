from django.contrib import admin
from Models_Demo.models_app.models import Student, University


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'level',
        'university'
    ]


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass

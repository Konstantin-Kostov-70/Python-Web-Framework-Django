from django.contrib import admin

from DjangoRESTDemo.demo_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
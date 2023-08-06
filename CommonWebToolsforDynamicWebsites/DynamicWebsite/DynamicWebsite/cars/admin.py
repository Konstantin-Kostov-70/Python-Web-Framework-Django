from django.contrib import admin
from DynamicWebsite.cars.models import Car


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    pass

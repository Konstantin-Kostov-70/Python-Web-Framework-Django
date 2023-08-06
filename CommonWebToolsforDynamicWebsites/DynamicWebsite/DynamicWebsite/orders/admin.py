from django.contrib import admin
from DynamicWebsite.orders.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass

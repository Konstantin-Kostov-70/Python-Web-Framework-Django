from django.contrib import admin

from DynamicWebsite.sales.models import Sale


@admin.register(Sale)
class AdminSale(admin.ModelAdmin):
    pass

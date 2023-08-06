from django.contrib import admin

from DynamicWebsite.buyers.models import Buyer


@admin.register(Buyer)
class AdminBuyer(admin.ModelAdmin):
    pass

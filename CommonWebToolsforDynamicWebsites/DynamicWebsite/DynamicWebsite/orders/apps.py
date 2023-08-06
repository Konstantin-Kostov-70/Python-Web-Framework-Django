from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DynamicWebsite.orders'

    def ready(self):
        import DynamicWebsite.orders.signals

from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DynamicWebsite.sales'

    def ready(self):
        import DynamicWebsite.sales.signals

from django.apps import AppConfig


class BuyersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DynamicWebsite.buyers'

    def ready(self):
        import DynamicWebsite.buyers.signals

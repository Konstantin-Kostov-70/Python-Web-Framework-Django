from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DynamicWebsite.cars'

    def ready(self):
        import DynamicWebsite.cars.signals

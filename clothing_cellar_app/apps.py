from django.apps import AppConfig


class ClothingCellarAppConfig(AppConfig):
    name = 'clothing_cellar_app'
    verbose_name = 'Ropa en bodega'

    def ready(self):
        try:
            import clothing_cellar_app.signals.clothing_cellar
        except ImportError:
            pass

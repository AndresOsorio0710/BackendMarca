from django.apps import AppConfig


class ProductCellarAppConfig(AppConfig):
    name = 'product_cellar_app'
    verbose_name = 'Productos en bodega'

    def ready(self):
        try:
            import product_cellar_app.signals.product_cellar
        except ImportError:
            pass

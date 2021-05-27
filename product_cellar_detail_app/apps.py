from django.apps import AppConfig


class ProductInCellarDetailAppConfig(AppConfig):
    name = 'product_in_cellar_detail_app'

    def ready(self):
        try:
            import product_in_cellar_detail_app.signals.product_in_cellar_detail
        except ImportError:
            pass

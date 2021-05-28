from rest_framework.routers import DefaultRouter
from product_cellar_sale_app.views import ProductCellarSaleViewSet

router = DefaultRouter()
router.register(r'pcs', ProductCellarSaleViewSet, basename='pcs')
urlpatterns = router.urls

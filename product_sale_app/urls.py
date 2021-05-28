from rest_framework.routers import DefaultRouter
from product_sale_app.views import ProductSaleViewSet

router = DefaultRouter()
router.register(r'ps', ProductSaleViewSet, basename='ps')
urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from product_cellar_app.views import ProductCellarViewSet

router = DefaultRouter()
router.register(r'pc', ProductCellarViewSet, basename='pc')
urlpatterns = router.urls

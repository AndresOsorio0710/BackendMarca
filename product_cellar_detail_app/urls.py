from rest_framework.routers import DefaultRouter
from product_in_cellar_detail_app.views import ProductInCellarDetailViewSet

router = DefaultRouter()
router.register(r'picd', ProductInCellarDetailViewSet, basename='picd')
urlpatterns = router.urls

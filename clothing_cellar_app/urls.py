from rest_framework.routers import DefaultRouter
from clothing_cellar_app.views import ClothingCellarViewSet

router = DefaultRouter()
router.register(r'clothing-c', ClothingCellarViewSet, basename='clothing-c')
urlpatterns = router.urls

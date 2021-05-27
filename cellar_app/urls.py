from rest_framework.routers import DefaultRouter
from cellar_app.views import CellarViewSet

router = DefaultRouter()
router.register(r'cellar', CellarViewSet, basename='cellar')
urlpatterns = router.urls

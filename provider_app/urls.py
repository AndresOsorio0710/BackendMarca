from rest_framework.routers import DefaultRouter
from provider_app.views import ProviderViewSet

router = DefaultRouter()
router.register(r'provider', ProviderViewSet, basename='provider')
urlpatterns = router.urls

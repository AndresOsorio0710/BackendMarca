from rest_framework.routers import DefaultRouter
from client_app.views import ClientViewSet

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
urlpatterns = router.urls

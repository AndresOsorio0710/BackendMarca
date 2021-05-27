from rest_framework.routers import DefaultRouter
from collection_app.views import CollectionViewSet

router = DefaultRouter()
router.register(r'collection', CollectionViewSet, basename='collection')
urlpatterns = router.urls

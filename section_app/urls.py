from rest_framework.routers import DefaultRouter
from section_app.views import SectionViewSet

router = DefaultRouter()
router.register(r'section', SectionViewSet, basename='section')
urlpatterns = router.urls

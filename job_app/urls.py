from rest_framework.routers import DefaultRouter
from job_app.views import JobViewSet

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')
urlpatterns = router.urls

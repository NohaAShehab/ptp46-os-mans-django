from students.api.views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students_view', StudentViewSet, basename='students_view')
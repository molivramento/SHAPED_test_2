from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.patients.views import PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

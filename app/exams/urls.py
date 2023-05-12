from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.exams.views import ExamViewSet

router = DefaultRouter()
router.register(r'exams', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

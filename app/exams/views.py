from app.exams.models import Exam
from rest_framework import viewsets, status
from rest_framework.response import Response
from SHAPED_test_2.celery import app as celery_app
from app.exams.serializers import ExamSerializer, ExamFilter


@celery_app.task
def save_exam(data):
    serializer = ExamSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    exam = serializer.save()
    return exam.id


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filterset_class = ExamFilter
    ordering = ['-date']

    def create(self, request, *args, **kwargs):
        exam_id = save_exam.delay(request.data)
        exam = Exam.objects.get(id=exam_id.get())
        serializer = self.get_serializer(exam)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
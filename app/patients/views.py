from app.patients.models import Patient
from rest_framework import viewsets, status
from rest_framework.response import Response
from celery import shared_task
from app.patients.serializers import PatientSerializer, PatientFilter


@shared_task
def save_patient(data):
    serializer = PatientSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    patient = serializer.save()
    return patient.id


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filterset_class = PatientFilter
    ordering_fields = ['name']
    ordering = ['name']

    def create(self, request, *args, **kwargs):
        patient_id = save_patient.delay(request.data)
        patient = Patient.objects.get(id=patient_id.get())
        serializer = self.get_serializer(patient)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

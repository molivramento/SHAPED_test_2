from rest_framework import viewsets
from app.patients.models import Patient
from app.patients.serializers import PatientSerializer, PatientFilter


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filterset_class = PatientFilter
    ordering_fields = ['name']
    ordering = ['name']

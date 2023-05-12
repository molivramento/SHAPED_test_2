from rest_framework import viewsets
from app.patients.models import Patient
from app.patients.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filterset_fields = ['name', 'birth_date', 'address']
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'birth_date', 'address']
    ordering = ['name']
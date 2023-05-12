from rest_framework import serializers
from app.patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'birth_date', 'address', 'get_age']
        read_only_fields = ['id', 'get_age']

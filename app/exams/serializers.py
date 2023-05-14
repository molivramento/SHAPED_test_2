from rest_framework import serializers
from app.exams.models import Exam
from django_filters import rest_framework as filters


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ['id']


class ExamFilter(filters.FilterSet):
    """
    Filter for Exam
    professional: str
    height_max: float
    height_min: float
    weight_max: int
    weight_min: int
    date_max: date (format: YYYY-MM-DD)
    date_min: date (format: YYYY-MM-DD)
    """
    professional = filters.CharFilter(field_name='professional', lookup_expr='icontains')
    height_max = filters.NumberFilter(field_name='height', lookup_expr='lte')
    height_min = filters.NumberFilter(field_name='height', lookup_expr='gte')
    weight_max = filters.NumberFilter(field_name='weight', lookup_expr='lte')
    weight_min = filters.NumberFilter(field_name='weight', lookup_expr='gte')
    date_max = filters.DateFilter(field_name='date', lookup_expr='lte')
    date_min = filters.DateFilter(field_name='date', lookup_expr='gte')
    patient = filters.CharFilter(field_name='patient__id', lookup_expr='exact')

    class Meta:
        model = Exam
        fields = ['height_max', 'height_min']

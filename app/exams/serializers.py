from rest_framework import serializers
from app.exams.models import Exam
from django_filters import rest_framework as filters


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ['id']


class ExamFilter(filters.FilterSet):
    height_max = filters.NumberFilter(field_name='height', lookup_expr='lte')
    height_min = filters.NumberFilter(field_name='height', lookup_expr='gte')

    class Meta:
        model = Exam
        fields = ['height_max', 'height_min']

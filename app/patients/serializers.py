import datetime

from rest_framework import serializers
from app.patients.models import Patient
from django_filters import rest_framework as filters


class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'birth_date', 'address', 'age']
        read_only_fields = ['id', 'age']

    def get_age(self, obj):
        return obj.get_age()


class PatientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    age_min = filters.NumberFilter(method='filter_age_min')
    age_max = filters.NumberFilter(method='filter_age_max')

    class Meta:
        model = Patient
        fields = ['name', 'age_min', 'age_max', 'address']

    def filter_age_min(self, queryset, name, value):
        return queryset.filter(birth_date__lte=datetime.date.today() - datetime.timedelta(days=int(value)*365))

    def filter_age_max(self, queryset, name, value):
        return queryset.filter(birth_date__gt=datetime.date.today() - datetime.timedelta(days=int(value+1)*365))

import datetime

from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=128)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_age(self):
        return int((datetime.date.today() - self.birth_date).days / 365)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        ordering = ['name']

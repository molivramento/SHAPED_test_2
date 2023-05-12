from django.db import models


class Exam(models.Model):
    professional = models.CharField(max_length=128)
    patient = models.ForeignKey('patients.Patient', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f'{self.professional} - {self.patient} - {self.date}'

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-date']

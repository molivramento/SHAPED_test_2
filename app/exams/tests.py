import json

from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from app.exams.models import Exam
from datetime import date
from app.patients.models import Patient


class ExamTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.exam1 = Exam.objects.create(
            patient=Patient.objects.create(
                name='Fulano', birth_date=date(2000, 1, 1), address='Rua do Fulano, 1'),
            date=date(2020, 1, 1), professional='Dr. Fulano', weight=80, height=1.80)
        self.exam2 = Exam.objects.create(
            patient=Patient.objects.create(
                name='Beltrano', birth_date=date(2000, 1, 1), address='Rua Beltrano, 3'),
            date=date(2020, 1, 1), professional='Dr. Beltrano', weight=80, height=1.80)

    def test_list_exams(self):
        response = self.client.get(reverse('exam-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_update_exam(self):
        data = {"description": "Exame 1"}
        response = self.client.patch(reverse('exam-detail', kwargs={'pk': self.exam2.id}), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Exam.objects.get(id=self.exam2.id).professional, 'Dr. Beltrano')

    def test_delete_exam(self):
        response = self.client.delete(reverse('exam-detail', kwargs={'pk': self.exam2.id}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Exam.objects.count(), 1)

    def test_filter_exam(self):
        response = self.client.get(reverse('exam-list'), {'height': 1.80})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['height'], 1.80)

    # def test_create_exam(self):
    #     response = self.client.get(reverse('exam-list'), {'id': 1})
    #     data = {
    #         "patient": response.data['results'][0],
    #         "date": "2020-01-01",
    #         "professional": "Dr. Ciclano",
    #         "weight": 80,
    #         "height": 1.80,
    #     }
    #     response = self.client.post(reverse('exam-list'), json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Exam.objects.count(), 3)
    #     self.assertEqual(Exam.objects.get(id=response.data['id']).weight, 80)

from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from app.patients.models import Patient
from datetime import date


class PatientTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.patient1 = Patient.objects.create(name='Fulano', birth_date=date(2000, 1, 1), address='Rua do Fulano, 1')
        self.patient2 = Patient.objects.create(name='Beltrano', birth_date=date(2000, 1, 1), address='Rua Beltrano, 3')
        self.patient3 = Patient.objects.create(name='Ciclano', birth_date=date(2000, 1, 1), address='Rua Ciclano, 5')
        self.patient4 = Patient.objects.create(name='Zé', birth_date=date(2000, 1, 1), address='Rua do Zé, 7')

    # Testing list and pagination
    def test_list_patients(self):
        response = self.client.get(reverse('patient-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

    def test_update_patient(self):
        data = {"name": "João"}
        response = self.client.patch(reverse('patient-detail', kwargs={'pk': self.patient4.id}), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Patient.objects.get(id=self.patient4.id).name, 'João')

    def test_delete_patient(self):
        response = self.client.delete(reverse('patient-detail', kwargs={'pk': self.patient4.id}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Patient.objects.count(), 3)

    def test_filter_patient(self):
        response = self.client.get(reverse('patient-list'), {'name': 'Beltr'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Beltrano')

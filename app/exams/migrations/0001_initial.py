# Generated by Django 4.2.1 on 2023-05-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.patient')),
            ],
            options={
                'verbose_name': 'Exam',
                'verbose_name_plural': 'Exams',
                'ordering': ['-date'],
            },
        ),
    ]

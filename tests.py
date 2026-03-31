from django.test import TestCase
from datetime import date, timedelta
from .models import Paciente, Doctor
# Create your tests here.

class PacienteModelTest(TestCase):

    def test_crear_paciente(self):
        paciente = Paciente.objects.create(
            nombre="Juan",
            apellido="Pérez",
            fecha_nacimiento=date(2000, 1, 1)
        )

        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")

def test_calculo_edad_paciente(self):
        fecha_nacimiento = date.today().replace(year=date.today().year - 20)

        paciente = Paciente.objects.create(
            nombre="Ana",
            apellido="Gómez",
            fecha_nacimiento=fecha_nacimiento
        )

        self.assertEqual(paciente.edad, 20)

def test_fecha_nacimiento_futura(self):
        fecha_futura = date.today() + timedelta(days=10)

        with self.assertRaises(ValueError):
            Paciente.objects.create(
                nombre="Pedro",
                apellido="López",
                fecha_nacimiento=fecha_futura
            )

class DoctorModelTest(TestCase):

    def test_crear_doctor(self):
        doctor = Doctor.objects.create(
            nombre="Carlos",
            apellido="Ramírez",
            fecha_nacimiento=date(1980, 5, 10),
            especialidad="CARD"
        )

        self.assertEqual(doctor.nombre, "Carlos")
        self.assertEqual(doctor.apellido, "Ramírez")

def test_calculo_edad_doctor(self):
        fecha_nacimiento = date.today().replace(year=date.today().year - 40)

        doctor = Doctor.objects.create(
            nombre="Laura",
            apellido="Soto",
            fecha_nacimiento=fecha_nacimiento,
            especialidad="DERM"
        )

        self.assertEqual(doctor.edad, 40)

def test_fecha_nacimiento_doctor_futura(self):
        fecha_futura = date.today() + timedelta(days=30)

        with self.assertRaises(ValueError):
            Doctor.objects.create(
                nombre="Mario",
                apellido="Ríos",
                fecha_nacimiento=fecha_futura,
                especialidad="GEN"
            )


from django.db import models
from datetime import date


# -------------------------
# PACIENTE
# -------------------------
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(editable=False)
    fecha_nacimiento = models.DateField()

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def save(self, *args, **kwargs):
        if self.fecha_nacimiento > date.today():
            raise ValueError("La fecha de nacimiento no puede ser futura.")
        self.edad = self.calcular_edad()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.edad} años)"


# -------------------------
# DOCTOR
# -------------------------
class Doctor(models.Model):

    ESPECIALIDADES = [
        ('CARD', 'Cardiología'),
        ('DERM', 'Dermatología'),
        ('PED', 'Pediatría'),
        ('GEN', 'Medicina General'),
        ('NEUR', 'Neurología'),
        ('TRAU', 'Traumatología'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(editable=False)
    fecha_nacimiento = models.DateField()
    especialidad = models.CharField(max_length=10, choices=ESPECIALIDADES)

    def calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def save(self, *args, **kwargs):
        if self.fecha_nacimiento > date.today():
            raise ValueError("La fecha de nacimiento no puede ser futura.")
        self.edad = self.calcular_edad()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.get_especialidad_display()}"


# -------------------------
# HORA MÉDICA
# -------------------------
class HoraMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200, blank=True)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} con {self.doctor}"

# -------------------------
# DÍAS BLOQUEADOS
# -------------------------
class DiaBloqueado(models.Model):
    fecha = models.DateField(unique=True)
    motivo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.motivo}"



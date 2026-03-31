from django import forms
from datetime import date, time, datetime, timedelta

from .models import Paciente, Doctor, HoraMedica, DiaBloqueado


# -------------------------
# FORMULARIO PACIENTE
# -------------------------
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'fecha_nacimiento',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }


# -------------------------
# FORMULARIO DOCTOR
# -------------------------

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'especialidad']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

# -------------------------
# FORMULARIO HORA MÉDICA
# -------------------------
class HoraMedicaForm(forms.ModelForm):

    # Horarios válidos: 08:00 a 13:00 cada 15 minutos
    HORA_CHOICES = []

    inicio = datetime.combine(date.today(), time(8, 0))
    fin = datetime.combine(date.today(), time(13, 0))

    actual = inicio
    while actual <= fin:
        HORA_CHOICES.append(
            (actual.time().strftime('%H:%M'), actual.time().strftime('%H:%M'))
        )
        actual += timedelta(minutes=15)

    hora = forms.ChoiceField(
        choices=HORA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = HoraMedica
        fields = ['paciente', 'doctor', 'fecha', 'hora', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'motivo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Control general, dolor lumbar, seguimiento…'
            })
}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = ['%Y-%m-%d']

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        hoy = date.today()

        # No pasado ni hoy
        if fecha <= hoy:
            raise forms.ValidationError(
                "La hora médica debe ser agendada para una fecha futura."
            )

        # No fines de semana
        if fecha.weekday() >= 5:
            raise forms.ValidationError(
                "No se atiende fines de semana."
            )

        # Días completos bloqueados
        if DiaBloqueado.objects.filter(fecha=fecha).exists():
            raise forms.ValidationError(
                "Este día no está disponible para atención."
            )

        return fecha

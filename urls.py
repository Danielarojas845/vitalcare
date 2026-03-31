from django.urls import path
from .views import (
    home,
    editar_paciente,
    eliminar_paciente,
    doctores,
    horas_medicas,
)

urlpatterns = [
    # Pacientes
    path("", home, name="home"),
    path("editar/<int:id>/", editar_paciente, name="editar_paciente"),
    path("eliminar/<int:id>/", eliminar_paciente, name="eliminar_paciente"),

    # Área médica
    path("doctores/", doctores, name="doctores"),
    path("horas/", horas_medicas, name="horas_medicas"),
]
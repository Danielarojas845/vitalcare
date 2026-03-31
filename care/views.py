from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Paciente, Doctor, HoraMedica
from .forms import PacienteForm, DoctorForm, HoraMedicaForm

def home(request):
    pacientes = Paciente.objects.all().order_by('-id')

    query = request.GET.get('buscar')
    if query:
        pacientes = pacientes.filter(
            nombre__icontains=query
        ) | pacientes.filter(
            apellido__icontains=query
        )

    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Paciente registrado correctamente"
            return render(request, 'core/home.html', {
                'form': PacienteForm(),
                'pacientes': pacientes,
                'mensaje': mensaje
            })
    else:
        form = PacienteForm()

    return render(request, 'core/home.html', {
        'form': form,
        'pacientes': pacientes
    })

@login_required
def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PacienteForm(instance=paciente)

    context = {"form": form, "paciente": paciente}

    return render(request, "core/editar_paciente.html", context)


@login_required
def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect("home")


@login_required
def doctores(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctores')
    else:
        form = DoctorForm()

    lista_doctores = Doctor.objects.all()

    return render(request, 'core/doctores.html', {
        'form': form,
        'doctores': lista_doctores
    })

@login_required
def horas_medicas(request):
    if request.method == "POST":
        form = HoraMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horas_medicas')
    else:
        form = HoraMedicaForm()

    horas = HoraMedica.objects.all().order_by('-fecha', '-hora')

    return render(request, 'core/horas_medicas.html', {
        'form': form,
        'horas': horas
    })



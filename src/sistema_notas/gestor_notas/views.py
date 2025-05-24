from django.shortcuts import render
from .forms import AlumnoForm, CursoForm, NotaAlumnoPorCursoForm
#  Create your views here.case


def agregar_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_alumno")
    else:
        form = AlumnoForm()
    return render(request, "gestor_notas/agregar_alumno.html", {"form": form})

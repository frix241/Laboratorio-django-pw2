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


def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_curso")
    else:
        form = CursoForm()
    return render(request, "gestor_notas/agregar_curso.html", {"form": form})


def agregar_nota(request):
    if request.method == "POST":
        form = NotaAlumnoPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_nota")
    else:
        form = NotaAlumnoPorCursoForm()
    return render(request, "gestor_notas/agregar_nota.html", {"form": form})

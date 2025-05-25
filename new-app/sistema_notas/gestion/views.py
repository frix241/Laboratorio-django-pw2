from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaAlumnoCursoForm
from .models import NotaAlumnoCurso

# Vista para crear un alumno
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'gestion/crear_alumno.html', {'form': form})

# Vista para crear un curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_curso')
    else:
        form = CursoForm()
    return render(request, 'gestion/crear_curso.html', {'form': form})

# Vista para registrar una nota
def crear_nota(request):
    if request.method == 'POST':
        form = NotaAlumnoCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaAlumnoCursoForm()
    return render(request, 'gestion/crear_nota.html', {'form': form})

# Vista para listar notas
def lista_notas(request):
    notas = NotaAlumnoCurso.objects.all()
    return render(request, 'gestion/lista_notas.html', {'notas': notas})

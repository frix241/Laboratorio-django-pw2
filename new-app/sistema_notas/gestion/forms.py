from django import forms
from .models import Alumno, Curso, NotaAlumnoCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class NotaAlumnoCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoCurso
        fields = ['alumno', 'curso', 'nota']

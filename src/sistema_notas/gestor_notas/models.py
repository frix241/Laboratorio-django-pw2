from django.db import models


# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cui = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}"

class NotaAlumnoPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - {self.curso}: {self.nota}"

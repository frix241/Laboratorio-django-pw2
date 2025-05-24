from django.urls import path
from . import views

urlspatterns = [
    path("alumno/", views.agregar_alumno, name="agregar_alumno"),
    path("curso/", views.agregar_curso, name="agregar_curso"),
    path("nota/", views.agregar_nota, name="agregar_nota"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('alumno/', views.crear_alumno, name='crear_alumno'),
    path('curso/', views.crear_curso, name='crear_curso'),
    path('nota/', views.crear_nota, name='crear_nota'),
    path('notas/', views.lista_notas, name='lista_notas'),
]

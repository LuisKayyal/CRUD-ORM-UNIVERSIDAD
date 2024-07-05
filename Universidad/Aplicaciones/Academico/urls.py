from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('editarCurso/', views.editarCurso),

    path('registrarEstudiante/', views.registrarEstudiante),
    path('gestionEstudiantes/', views.gestionEstudiantes),
    path('edicionEstudiante/<codigo>', views.edicionEstudiante),
    path('eliminarEstudiante/<codigo>', views.eliminarEstudiante),
    path('editarEstudiante/', views.editarEstudiante),

    path('registrarDocente/', views.registrarDocente),
    path('gestionDocentes/', views.gestionDocentes),
    path('edicionDocente/<codigo>', views.edicionDocente),
    path('eliminarDocente/<codigo>', views.eliminarDocente),
    path('editarDocente/', views.editarDocente),
]

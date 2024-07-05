from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
    
class Estudiante(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50, default="N/A")
    email = models.EmailField(default="N/A")
    telefono = models.CharField(max_length=15, default="N/A")
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50, default="N/A")
    email = models.EmailField(default="N/A")
    telefono = models.CharField(max_length=15, default="N/A")
    cursos = models.ManyToManyField(Curso, related_name='docentes')

    def __str__(self):
        return self.nombre

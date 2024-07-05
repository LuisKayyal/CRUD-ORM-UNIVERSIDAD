from django.shortcuts import get_object_or_404, render, redirect
from .models import Curso, Estudiante, Docente
from django.contrib import messages

# Vistas para Cursos, Estudiante y Docente
def home(request):
    cursosListados = Curso.objects.all()
    estudiantesListados = Estudiante.objects.all()
    docentesListados = Docente.objects.all()

    messages.success(request, '¡Datos Listados!')

    return render(request, "gestionCursos.html", {
        "cursos": cursosListados,
        "estudiantes": estudiantesListados,
        "docentes": docentesListados,
    })

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')
    return redirect('/')

# Vistas para Estudiantes
def registrarEstudiante(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']

    estudiante = Estudiante.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, 
                                           email=email, telefono=telefono)
    messages.success(request, '¡Estudiante registrado!')
    return redirect('/')

def gestionEstudiantes(request):
    estudiantesListados = Estudiante.objects.all()
    messages.success(request, '¡Estudiantes Listados!')
    return render(request, "gestionEstudiantes.html", {"estudiantes": estudiantesListados})

def edicionEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

def editarEstudiante(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']

    estudiante = Estudiante.objects.get(codigo=codigo)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.email = email
    estudiante.telefono = telefono
    estudiante.save()

    messages.success(request, '¡Estudiante actualizado!')
    return redirect('/')

def eliminarEstudiante(request, codigo):
    estudiante = get_object_or_404(Estudiante, codigo=codigo)
    estudiante.delete()

    messages.success(request, '¡Estudiante eliminado!')
    return redirect('/')

# Vistas para Docentes
def registrarDocente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']

    docente = Docente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, 
                                     email=email, telefono=telefono)
    messages.success(request, '¡Docente registrado!')
    return redirect('/')

def gestionDocentes(request):
    docentesListados = Docente.objects.all()
    messages.success(request, '¡Docentes Listados!')
    return render(request, "gestionDocentes.html", {"docentes": docentesListados})

def edicionDocente(request, codigo):
    docente = Docente.objects.get(codigo=codigo)
    return render(request, "edicionDocente.html", {"docente": docente})

def editarDocente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    telefono = request.POST['txtTelefono']

    docente = Docente.objects.get(codigo=codigo)
    docente.nombre = nombre
    docente.apellido = apellido
    docente.email = email
    docente.telefono = telefono
    docente.save()

    messages.success(request, '¡Docente actualizado!')
    return redirect('/')

def eliminarDocente(request, codigo):
    docente = get_object_or_404(Docente, codigo=codigo)
    docente.delete()

    messages.success(request, '¡Docente eliminado!')
    return redirect('/')
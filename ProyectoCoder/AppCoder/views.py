from .models import Curso
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def curso(request, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse ( f"""
        <p>Curso: {curso.nombre} agregado </p>
    """)

def lista_cursos(request):

    lista = Curso.objects.all()

    return render(request, "lista_cursos.html", {"lista_cursos": lista} )
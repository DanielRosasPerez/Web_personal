from django.shortcuts import render
from .models import Project

# Create your views here.

def portafolio(request):
    projects = Project.objects.all() # Nos devuelve todos los objetos que tiene el modelo de proyecto.
    return render(request, "portafolio/portafolio.html", {"projects":projects})
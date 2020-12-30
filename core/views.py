from django.shortcuts import render, HttpResponse # El método "HttpResponse" nos permite contestar a una petición devolviendo un código.

# Create your views here.
def home(request):
    #return HttpResponse("<h2>Hola, Bienvenido</h2>")
    return render(request, "core/home.html") # render(request, "<ruta_aplicación>")

def about(request):
    return render(request, "core/about.html")

def contacto(request):
    return render(request, "core/contacto.html")



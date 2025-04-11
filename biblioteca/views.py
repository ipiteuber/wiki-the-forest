from django.shortcuts import render

# Create your views here.
def menuprincipal_wiki(request):
    return render(request, 'wiki/menuprincipal_wiki.html')

def armas(request):
    return render(request, 'wiki/armas.html')

def construcciones(request):
    return render(request, 'wiki/construcciones.html')

def consumibles(request):
    return render(request, 'wiki/consumibles.html')

def flora(request):
    return render(request, 'wiki/flora.html')

def enemigos(request):
    return render(request, 'wiki/enemigos.html')

def lugarestf(request):
    return render(request, 'wiki/lugarestf.html')

def logros(request):
    return render(request, 'wiki/logros.html')

def animales(request):
    return render(request, 'wiki/animales.html')

def historia(request):
    return render(request, 'wiki/historia.html')

def forowiki(request):
    return render(request, 'wiki/forowiki.html')

def inicio_sesion_wiki(request):
    return render(request, 'wiki/inicio_sesion_wiki.html')

def registrase_wiki(request):
    return render(request, 'wiki/registrase_wiki.html')

def recuperarcontra(request):
    return render(request, 'wiki/recuperarcontra.html')

def micuentatf(request):
    return render(request, 'wiki/micuentatf.html')
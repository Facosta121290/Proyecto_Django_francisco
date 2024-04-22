from django.shortcuts import render

# Create your views here.
from . import models

def home(request):
    consulta_productos = models.ProductoCategoria.objects.all()
    context = {"productos": consulta_productos} # clientes es la clave
    return render(request, "producto/index.html", context)
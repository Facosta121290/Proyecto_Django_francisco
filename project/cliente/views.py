from django.shortcuts import render

# Create your views here.
from . import models

def home(request):
    consulta_clientes = models.Cliente.objects.all()
    context = {"clientes": consulta_clientes} # clientes es la clave
    return render(request, "cliente/index.html", context)
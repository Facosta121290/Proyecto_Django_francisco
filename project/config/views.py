from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render #Esta función permite realizar un atajo

def saludo(request):
    return HttpResponse("¡Hola Django!")

def saludo2(request):
    return HttpResponse("<h1>¡Hola Francisco Acosta!</h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
    mi_html = open("./templates/template1.html", encoding="UTF-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo": "¡Bienvenido!", 
                           "clase": "CoderHouse"})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def mis_notas(request):
    lista_de_notas = [2, 3, 5, 7, 9, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)

def ver_persona(request):
    contexto = {
        "persona": {
            "nombre": "Francisco",
            "edad": "33",
            },
        }
    return render(request, "personas.html", contexto)
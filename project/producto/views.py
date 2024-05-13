from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

def home(request):

    return render(request, "producto/index.html")

# LIST
# def productocategoria_list(request):
#     consulta = request.GET.get("consulta", None)

#     if consulta:
#         print(consulta)
#         query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
#     else:
#         query = models.ProductoCategoria.objects.all()

#     context = {"productos": query}
#     return render(request, "producto/productocategoria_list.html", context)

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"


# CREATE
# def productocategoria_create(request):
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:home")
#     else: # request.method == "GET"
#         form = forms.ProductoCategoriaForm()
#     return render(request, "producto/productocategoria_create.html", context={"form": form})

class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")


# DETAIL
# def productocategoria_detail(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", {"producto": query})

class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    # context_object_name = "producto"

# UPDATE
# def productocategoria_update(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = forms.ProductoCategoriaForm(request.POST, instance=query)
#         if form.is_valid:
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else: # request.method == "GET"
#         form = forms.ProductoCategoriaForm(instance=query)
#     return render(request, "producto/productocategoria_update.html", context={"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# DELETE
# def productocategoria_delete(request, pk: int):
#     query = models.ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_delete.html", context={"producto": query})

class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("producto:productocategoria_list")


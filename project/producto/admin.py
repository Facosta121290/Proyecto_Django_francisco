from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Productos"


class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", )

admin.site.register(models.ProductoCategoria, ProductoCategoriaAdmin)

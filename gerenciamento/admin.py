from django.contrib import admin
from .models import Clientes, Marcas, Fornecedores

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Marcas)
admin.site.register(Fornecedores)
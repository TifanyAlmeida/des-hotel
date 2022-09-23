from django.contrib import admin
from .models import Hospedadore, Hospedagen, Endereco, ListaRecurso, Recurso

admin.site.register(Hospedagen)
admin.site.register(Endereco)
admin.site.register(ListaRecurso)
@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ["nome_recurso"]
admin.site.register(Hospedadore)
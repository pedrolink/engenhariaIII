from django.contrib import admin
from . import models


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_nascimento', 'cpf',
                    'tipo_perfil', 'cidade', 'estado')

    list_filter = ['tipo_perfil']


admin.site.register(models.Perfil, PerfilAdmin)

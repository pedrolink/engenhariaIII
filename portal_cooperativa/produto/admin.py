from django.contrib.admin.decorators import display
from produto.models import Produto
from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_preco_formatado',
                    'get_preco_promocional_formatado']
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
admin.site.register(models.Categoria)
admin.site.register(models.Fornecedor)

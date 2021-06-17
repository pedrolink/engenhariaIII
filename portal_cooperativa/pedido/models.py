from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    id_fornecedor = models.PositiveIntegerField()
    total = models.FloatField()
    observacao = models.TextField(max_length=255, verbose_name='Observação')
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Nº Pedido: {self.pk}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    categoria = models.CharField(max_length=255)
    id_categoria = models.PositiveIntegerField()
    preco = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(
        default=0, verbose_name='Preço Promocional')
    quantidade = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.pedido}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'

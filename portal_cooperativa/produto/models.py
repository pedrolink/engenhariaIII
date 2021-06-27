from produto.templatetags.omfilters import formata_preco
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify
from utils import utils
from django.contrib.auth.models import User
from utils.validacnpj import valida_cnpj
from django.forms import ValidationError


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

    def clean(self):
        error_messages = {}

        cnpj_enviado = self.cnpj or None
        cnpj_salvo = None
        fornecedor = Fornecedor.objects.filter(cnpj=cnpj_enviado).first()

        if fornecedor:
            cnpj_salvo = fornecedor.cnpj

            if cnpj_salvo is not None and self.pk != fornecedor.pk:
                error_messages['cnpj'] = 'CNPJ já existe.'

        if not valida_cnpj(self.cnpj):
            error_messages['cnpj'] = 'Digite um CNPJ válido.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(
        max_length=255, verbose_name='Descrição Curta')
    descricao_longa = models.TextField(verbose_name='Descrição Longa')
    preco = models.FloatField(default=0, verbose_name='Preço')
    preco_promocional = models.FloatField(
        default=0, verbose_name='Preço Promocional')
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variação'),
            ('S', 'Simples'),
        )
    )
    id_fornecedor = models.ForeignKey(
        Fornecedor, on_delete=models.CASCADE, verbose_name='Usuário Fornecedor')

    def get_preco_formatado(self):
        return formata_preco(self.preco)

    def get_preco_promocional_formatado(self):
        return formata_preco(self.preco_promocional)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

# Generated by Django 3.2.4 on 2021-06-24 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_qtd_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='variacao',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itempedido',
            name='variacao_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

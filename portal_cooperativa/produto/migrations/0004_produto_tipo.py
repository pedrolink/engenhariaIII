# Generated by Django 3.2.4 on 2021-06-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variação'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
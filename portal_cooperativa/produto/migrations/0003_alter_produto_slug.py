# Generated by Django 3.2.4 on 2021-06-14 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210609_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

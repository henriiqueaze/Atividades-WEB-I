# Generated by Django 5.1.9 on 2025-05-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('tipo', models.CharField(choices=[('vaso', 'Vaso'), ('flor', 'Flor'), ('planta', 'Planta Medicinal'), ('semente', 'Semente'), ('ferramenta', 'Ferramenta de Jardim')], default='vaso', max_length=20, verbose_name='Tipo')),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Preço')),
                ('quantidade', models.PositiveIntegerField(default=0, verbose_name='Quantidade')),
                ('descricao', models.TextField(blank=True, default='', verbose_name='Descrição')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='produtos/', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['name'],
            },
        ),
    ]

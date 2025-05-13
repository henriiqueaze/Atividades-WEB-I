from django.db import models
from django.urls import reverse

class Product(models.Model):
    TIPO_CHOICES = [
        ('vaso', 'Vaso'),
        ('flor', 'Flor'),
        ('planta', 'Planta Medicinal'),
        ('semente', 'Semente'),
        ('ferramenta', 'Ferramenta de Jardim'),
    ]

    name = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', max_length=20, choices=TIPO_CHOICES, default='vaso')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, default=0.00)
    quantidade = models.PositiveIntegerField('Quantidade', default=0)
    descricao = models.TextField('Descrição', blank=True, default='')
    foto = models.ImageField('Foto', upload_to='produtos/', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f"{self.name} ({self.get_tipo_display()})"

    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})

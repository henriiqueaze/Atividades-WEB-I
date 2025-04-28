from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    ano_lancamento = models.IntegerField()
    imagem = models.ImageField(upload_to='filmes/')

    def __str__(self):
        return self.titulo

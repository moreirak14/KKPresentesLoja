from django.db import models

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=200)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome

class Marcas(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Fornecedores(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=200)
    observacoes = models.TextField()

    def __str__(self):
        return self.nome + ' - ' + self.marca.nome

from secrets import choice
from unicodedata import decimal
from django.db import models

# arrumar o vista para que seja possivel escolher mais de um

#ENDERECO
class Endereco(models.Model):
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.pais

#HOSPEDADOR
class Hospedadore(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    sobre = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='foto/%y/%m/%d')

    def __str__(self):
        return self.nome

#LISTA DE RECURSO
class ListaRecurso(models.Model):
    tipo_recurso = models.CharField(max_length=60)

    def __str__(self):
        return self.tipo_recurso

#RECURSO
class Recurso(models.Model):

    nome_recurso = models.CharField(max_length=60)
    lista_recurso = models.ManyToManyField(ListaRecurso)

    def __str__(self):
        return self.nome_recurso

#lembrar de botar cascacade
D = 'Dia'
S = 'Semana'
M = 'Mês'
PERIODO_CHOICES = [
    (D, 'Dia'),
    (S, 'Semana'),
    (M, 'Mês'),
]

class Hospedagen(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    preco_por = models.CharField(choices=PERIODO_CHOICES, max_length=6, default=D)
    taxa_limpeza = models.DecimalField(decimal_places=2, max_digits=8)
    imagem_1 = models.ImageField(upload_to='foto/%y/%m/%d')
    imagem_2 = models.ImageField(upload_to='foto/%y/%m/%d')
    imagem_3 = models.ImageField(upload_to='foto/%y/%m/%d')
    imagem_4 = models.ImageField(upload_to='foto/%y/%m/%d')
    imagem_5 = models.ImageField(upload_to='foto/%y/%m/%d')
    disponibilidade_a_partir = models.DateField()
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    lista_recurso = models.ForeignKey(Recurso, on_delete=models.PROTECT)
    hospedador = models.ForeignKey(Hospedadore, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.titulo
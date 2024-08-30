from django.db import models

# Create your models here.
class FunCadastrarAnimal(models.Model):
    nome = models.CharField(max_length=80)
    idtutor = models.IntegerField(max_length=80)
    raca = models.CharField(max_length=80)
    idade = models.IntegerField(max_length=3)
    especie = models.CharField(max_length=80)
    doenca = models.BooleanField(max_length=10)
    qual = models.CharField(max_length=80)

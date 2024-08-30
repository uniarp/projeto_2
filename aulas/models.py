from django.db import models

# Create your models here.
class Doenca(models.Model):
    nomeDoenca = models.CharField(max_length=80)
    sintomas = models.CharField(max_length=80)
    trat_associados = models.CharField(max_length=80)



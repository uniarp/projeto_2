from django.db import models

# Create your models here.
class Doenca(models.Model):
    nomeDoenca = models.CharField(max_length=80)
    sintomas = models.CharField(max_length=80)
    trat_associados = models.CharField(max_length=80)

class Tutor(models.Model):
    nome = models.Charfield(max_lenght=80)
    sobrenome = models.Charfield(max_lenght=80)
    rua = models.Charfield(max_lenght=80)
    bairro = models.Charfield(max_lenght=80)
    num = models.Charfield(max_lenght=8)
    cidade = models.Charfield(max_lenght=80)
    estado = models.Charfield(max_lenght=80)
    cep = models.Charfield(max_lenght=12)
    email = models.Charfield(max_lenght=60)
    telefone = models.Charfield(max_lenght=12)
    cpf = models.Charfield(max_lenght=14)
    idTutor = models.IntegerField((max_lenght=80)primary_key=true)
    def cadastrarTutor(self):
        #logica de cadastro tutor
        
        



from django.db import models

class Animal(models.Model):
    id_animal = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    id_tutor = models.IntegerField()
    raca = models.CharField(max_length=80)
    idade = models.IntegerField()
    especie = models.CharField(max_length=80)
    doenca = models.BooleanField()

def cadastrarAnimal(self, nome, especie, id_tutor, raca, idade, id_doenca=None):
    animal = Animal(
        nome=nome,
        especie=especie,
        id_tutor=id_tutor,
        raca=raca,
        idade=idade,
        id_doenca=id_doenca
    )
    animal.save()
    return animal.id_animal

def __str__(self):
    return f"{self.nome} ({self.especie})"
from django.db import models
from django.core.exceptions import ValidationError
import re

def validarNome(value):
    if not re.match(r'^[A-Za-zÀ-öø-ÿÇç\s]+$',value):
        raise ValidationError('O nome deve conter apenas letras e espaços')
    
class id_Tutor(models.Model): #apenas exemplo para validar tutor
    nome = models.CharField(max_length=100)


class Animal(models.Model):
    ESPECIES_CHOICES = [
        ('CACHORRO', 'Cachorro'),
        ('GATO', 'Gato'),
        ('COELHO', 'Coelho'),
        ('PASSÁRO', 'Passáro'),
    ]

    SEXO_CHOICES = [
        ('MACHO', 'Macho'),
        ('FÊMEA', 'Fêmea'),
    ]

    id_animal = models.AutoField(primary_key=True, blank=False)
    id_tutor = models.ForeignKey(id_Tutor, on_delete=models.CASCADE, null=False)
    nome = models.CharField(max_length=80, validators=[validarNome])
    sexo = models.CharField(max_length=10) #usar choice em algum momento
    raca = models.CharField(max_length=80)
    especie = models.CharField(max_length=80)
    pelagem = models.CharField(max_length=20)
    idade = models.PositiveIntegerField()
   # id_doenca = models.ForeignKey()


def clean(self):
    super().clean()
    if self.idade <= 0:
        raise ValidationError (' A idade deve ser positiva')

def cadastrarAnimal(self, nome, especie, id_tutor, raca, idade, id_doenca=None):
    animal = Animal(
        nome=nome,
        especie=especie,
        id_tutor=id_tutor,
        raca=raca,
        idade=idade,
        id_doenca=id_doenca
    )
    animal.full_clean()
    animal.save()
    return animal.id_animal


def __str__(self):
    return f"{self.nome} ({self.especie})"
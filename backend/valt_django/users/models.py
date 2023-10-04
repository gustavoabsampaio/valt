from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True, null=True, blank=True)
    nascimento = models.DateField()


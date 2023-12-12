from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    nascimento = models.DateField()


    REQUIRED_FIELDS = ['cpf', 'email', 'nascimento']
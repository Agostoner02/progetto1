from django.db import models


class Contatto(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contenuto = models.CharField(max_length=200)

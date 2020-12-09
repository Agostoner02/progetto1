from django.db import models

# Create your models here.

class Genere(models.Model):
    nome = models.CharField(max_length=20)

    def _str_(self):
        return self.nome

class Autore(models.Model):
    nome = models.CharField(max_length=20)
    conome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def _str_(self):
        return self.nome + " " + self.cognome

class Libro(models.Model):
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = model.ForeignKey(Autore, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere)

    def _str_(self):
        return self.titolo
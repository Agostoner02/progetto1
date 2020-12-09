from django.db import models

# Create your models here.

class Genere_AL(models.Model):
    nome = models.CharField(max_length=20)

    def _str_(self):
        return self.nome

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Autore_AL(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def _str_(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class Libro_AL(models.Model):
    titolo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(Libro_AL, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Libro_AL)

    def _str_(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"
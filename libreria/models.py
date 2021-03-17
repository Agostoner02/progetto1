from django.db import models


class GenereAL(models.Model):
    nome = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Genere'
        verbose_name_plural = 'Generi'

    def __str__(self):
        return self.nome


class AutoreAL(models.Model):
    nome = models.CharField(max_length=50)
    nazione = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

    def __str__(self):
        return self.nome


class LibroAL(models.Model):
    titolo = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    autore = models.ForeignKey(
        AutoreAL, on_delete=models.CASCADE, related_name="libri")
    generi = models.ManyToManyField(GenereCD)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libri'

    def __str__(self):
        return self.titolo

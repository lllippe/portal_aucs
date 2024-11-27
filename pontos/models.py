from django.db import models


class Ponto(models.Model):
    titulo = models.CharField(max_length=30)
    arquivo = models.CharField(max_length=10)
    linha = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


class Letra(models.Model):
    ponto = models.ForeignKey(Ponto, on_delete=models.CASCADE)
    letra0 = models.CharField(max_length=60, blank=True, null=True)
    letra1 = models.CharField(max_length=60, blank=True, null=True)
    letra2 = models.CharField(max_length=60, blank=True, null=True)
    letra3 = models.CharField(max_length=60, blank=True, null=True)
    letra4 = models.CharField(max_length=60, blank=True, null=True)
    letra5 = models.CharField(max_length=60, blank=True, null=True)
    letra6 = models.CharField(max_length=60, blank=True, null=True)
    letra7 = models.CharField(max_length=60, blank=True, null=True)
    letra8 = models.CharField(max_length=60, blank=True, null=True)
    letra9 = models.CharField(max_length=60, blank=True, null=True)

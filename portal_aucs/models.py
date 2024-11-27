from django.db import models


class calendario(models.Model):
    titulo = models.CharField(max_length=40)
    data = models.CharField(max_length=10)
    horario = models.CharField(max_length=10)
    status = models.CharField(max_length=1)
    obs = models.CharField(max_length=100)
    imagem = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class eventos(models.Model):
    titulo = models.CharField(max_length=40)
    data = models.CharField(max_length=10)
    horario = models.CharField(max_length=10)
    obs = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

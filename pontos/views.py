from django.shortcuts import render
from pontos.models import Ponto, Letra


def pontos(request):
    pontos = Ponto.objects.all().order_by('linha')
    linhas = []
    elements_dark = []

    for x in pontos:
        if x.linha not in linhas:
            linhas.append(x.linha.strip())

    for y in linhas:
        if linhas.index(y) % 2:
            elements_dark.append(y.strip())

    context = {
        'ponto': pontos,
        'linha': linhas,
        'dark': elements_dark
    }
    return render(request, 'pontos/index.html', context)


def letra(request, ponto):
    letras = Letra.objects.all()
    valueOk = False

    for x in letras:
        if str(x.ponto) == ponto:
            valueOk = True
    context = {
        'letra': letras,
        'ponto': ponto,
        'value': valueOk
    }
    return render(request, 'pontos/letra.html', context)

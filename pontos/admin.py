from django.contrib import admin
from .models import Ponto, Letra


class Pontos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'arquivo', 'linha')
    list_display_links = ('id',)
    search_fields = ('titulo', 'arquivo', 'linha')
    list_filter = ('titulo', 'arquivo', 'linha')
    list_editable = ('titulo', 'arquivo', 'linha')
    list_per_page = 10


admin.site.register(Ponto, Pontos)


class Letras(admin.ModelAdmin):
    list_display = ('id', 'ponto', 'letra0', 'letra1', 'letra2', 'letra3', 'letra4', 'letra5', 'letra6', 'letra7',
                    'letra8', 'letra9')
    list_display_links = ('id',)
    search_fields = ('ponto', 'letra0', 'letra1', 'letra2', 'letra3', 'letra4', 'letra5', 'letra6', 'letra7',
                     'letra8', 'letra9')
    list_filter = ('ponto', 'letra0', 'letra1', 'letra2', 'letra3', 'letra4', 'letra5', 'letra6', 'letra7',
                   'letra8', 'letra9')
    list_editable = ('ponto', 'letra0', 'letra1', 'letra2', 'letra3', 'letra4', 'letra5', 'letra6', 'letra7',
                     'letra8', 'letra9')
    list_per_page = 10


admin.site.register(Letra, Letras)

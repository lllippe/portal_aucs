from django.contrib import admin
from .models import calendario, eventos


class Calendarios(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data', 'horario', 'status', 'obs', 'imagem')
    list_display_links = ('id',)
    search_fields = ('titulo', 'data', 'horario', 'status', 'obs')
    list_filter = ('titulo', 'data', 'horario', 'status', 'obs')
    list_editable = ('titulo', 'data', 'horario', 'status', 'obs', 'imagem')
    list_per_page = 10


admin.site.register(calendario, Calendarios)


class Eventos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data', 'horario', 'obs')
    list_display_links = ('id',)
    search_fields = ('titulo', 'data', 'horario', 'obs')
    list_filter = ('titulo', 'data', 'horario', 'obs')
    list_editable = ('titulo', 'data', 'horario', 'obs')
    list_per_page = 10


admin.site.register(eventos, Eventos)

from django.shortcuts import render
from portal_aucs.models import calendario, eventos
from datetime import datetime


def index(request):
    calendario_eventos = calendario.objects.all().order_by('data')
    eventos_data = eventos.objects.all().order_by('data')
    list_calendario = []
    list_eventos = []

    date = datetime.today().strftime('%d%m%Y')
    date1 = datetime.strptime(date, '%d%m%Y')

    for y in calendario_eventos:
        date2 = datetime.strptime(y.data[:2]+y.data[3:5]+y.data[6:10], '%d%m%Y')
        if date2 >= date1:
            calendario_limpo_obj = calendario()
            calendario_limpo_obj.titulo = y.titulo
            calendario_limpo_obj.data = y.data
            calendario_limpo_obj.horario = y.horario
            calendario_limpo_obj.status = y.status
            calendario_limpo_obj.obs = y.obs
            calendario_limpo_obj.imagem = y.imagem
            list_calendario.append(calendario_limpo_obj)

    for x in eventos_data:
        date3 = datetime.strptime(x.data[:2] + x.data[3:5] + x.data[6:10], '%d%m%Y')
        if date3 >= date1:
            eventos_limpo_obj = eventos()
            eventos_limpo_obj.titulo = x.titulo
            eventos_limpo_obj.data = x.data
            eventos_limpo_obj.horario = x.horario
            eventos_limpo_obj.obs = x.obs
            list_eventos.append(eventos_limpo_obj)

    calendario_exists = True if len(list_calendario) > 0 else False
    eventos_exists = True if len(list_eventos) > 0 else False

    context = {
        'calendario': list_calendario,
        'eventos': list_eventos,
        'data': date,
        'calendario_exists': calendario_exists,
        'eventos_exists': eventos_exists
    }

    return render(request, 'index.html', context)

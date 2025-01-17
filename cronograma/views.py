from django.shortcuts import render
from cronograma.data import events
# Create your views here.

context = {
    'pagina_ativa': 'cronograma',
    'titulo': 'CRONOGRAMA SEMANA DA JUVENTUDE',
    'events': events,
}

def cronograma(request):
    return render(
        request,
        'cronograma.html',
        context,
    )
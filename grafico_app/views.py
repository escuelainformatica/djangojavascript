from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from grafico_app.models import Valores


def grafico(request):
    contexto={}
    return render(request,'pagina.html',contexto)

def api_datos(request):

    query=Valores.objects.order_by('-id').first()

    datos={"campo1":query.campo1,"campo2":query.campo2,"campo3":query.campo3}
    return JsonResponse(datos,safe=False)

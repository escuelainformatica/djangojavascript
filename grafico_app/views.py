import datetime
import uuid

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from grafico_app.models import Valores, Tokens


def grafico(request):
    contexto = {}
    return render(request, 'pagina.html', contexto)


def api_datos(request:WSGIRequest):
    tokenleido=None
    try:
        if request.method=='POST':
            tokenleido = request.POST['token']
        else:
            tokenleido=request.GET['token']
    except:
        tokenleido=None
    try:
        if tokenleido==None:
            tokenleido=request.headers['token']
    except:
        tokenleido=None

    buscartoken=Tokens.objects.filter(uuid=tokenleido).first()

    if buscartoken==None:
        return JsonResponse({"error":"el token no existe"})

    ahora=datetime.datetime.now()

    diferencia=(ahora.timestamp()-buscartoken.fecha.timestamp())/60 # en minutos
    if diferencia  > 1:
        return JsonResponse({"error": "el token expiro hace "+str((diferencia)-1) +" minutos"})


    query = Valores.objects.order_by('-id').first()
    datos = {"campo1": query.campo1, "campo2": query.campo2, "campo3": query.campo3,"dif":diferencia}
    return JsonResponse(datos, safe=False)

def api_obtener_token(request:WSGIRequest):
    uuidOne = uuid.uuid1()
    fecha=datetime.datetime.now()
    nuevo= Tokens()
    nuevo.uuid=uuidOne
    nuevo.fecha=fecha
    nuevo.save()
    return JsonResponse({"token":uuidOne,"fecha":fecha},safe=False)

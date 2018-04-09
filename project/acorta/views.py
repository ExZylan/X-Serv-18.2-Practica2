from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Url

formulario = """
    <form action="/" method="POST">
    Url:<br>
    <input type="text" name="URL" value=""><br>
    <input type="submit" value="Enviar">
</form>
"""

def CompletaUrl(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return "http://" + url


def EncuentraUrl(url, found):
    if url != " ":
        lista = Url.objects.all()
        for web in lista:
            web = str(web)
            if web  == url:
                found = True
    print(found)
    return found


@csrf_exempt
def barra(request):
    found = False
    if request.method == "POST":
        url = Url(Direccion = request.POST['URL'])
        url = str(url)
        url = CompletaUrl(url)
        found = EncuentraUrl(url, found)
        if found != True:
            url = Url(Direccion = url)
            url.save()
    lista = Url.objects.all()
    if not found:
        salida = "<ul>"
        for url in lista:
            salida += '<li><a href="' + url.Direccion + '">' + str(url.id) + ", " + url.Direccion + '</a>'
        salida += "</ul>"
        salida = "<html><body><h1>" + formulario + "</h1><p>" + salida  + "</p></body></html>"
    else:
        salida = "<ul>"
        salida += '<li><a href="' + str(url) + '">' + str(url) + '</a>'
        salida += "</ul>"

    #salida += formulario

    return HttpResponse(salida)
from django.http import HttpResponse
from django.template import Template, Context
import datetime

def hello(request):
    doc_hello = open("C:/Users/ramnd/Desktop/curso-django-pildoras-info/project1/project1/templates/hello.html")
    plt_hello = Template(doc_hello.read())            #leemos el template
    doc_hello.close()                                 #cerramos el documento
    ctx_hello = Context()                             #creamos el contexto
    documento = plt_hello.render(ctx_hello)           #renderizamos
    return HttpResponse(documento)                    #retornamos el documento renderizado

def bye(request):
    doc_bye = open("C:/Users/ramnd/Desktop/curso-django-pildoras-info/project1/project1/templates/bye.html")
    plt_bye = Template(doc_bye.read())
    doc_bye.close()
    ctx_bye = Context()
    documento = plt_bye.render(ctx_bye)
    return HttpResponse(documento)
def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    fecha = """
        <html>
            <body>
                <h2>
                    fecha y hora actuales: %s
                </h2>
            </body>
        </html>
    """ % fecha_actual
    return HttpResponse(fecha)
def calculaEdad(request, nacim, agno):
    edadActual = nacim
    periodo = agno - 2021
    edadFutura = edadActual + periodo
    fechaFutura = """
        <html>
            <body>
                <h2>
                    tu edad en el ano %s sera: %s
                </h2>
            </body>
        </html>
    """ % (agno, edadFutura)
    return HttpResponse(fechaFutura)
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import datetime

class Person(object):
    def __init__(self, nombre, apellido, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera

def hello(request):
    p1 = Person("juan", "guzman", "sistemas")
    materias = ["Python", "Django", "JavaScript", "CSS", "HTML:5", "Angular 2+", "SqLite3"]

    doc_hello = loader.get_template('hello.html')    # ------metodo simple para cargar la plantilla paso 1-------
    docume = doc_hello.render({"nombre_persona": p1.nombre,
                                  "apellido_persona": p1.apellido,
                                  "carrera_persona": p1.carrera,
                                  "materias_persona": materias
                                  })          # ------metodo simple para cargar la plantilla paso 2-------
    return HttpResponse(docume)

def bye(request):
    p2 = Person("pedro", "diaz", "informatica")
    doc_bye = open("C:/Users/ramnd/Desktop/curso-django-pildoras-info/project1/project1/templates/bye.html")
    plt_bye = Template(doc_bye.read())
    doc_bye.close()
    ctx_bye = Context({"nombre_persona": p2.nombre,
                       "apellido_persona": p2.apellido,
                       "carrera_persona": p2.carrera})
    documento = plt_bye.render(ctx_bye)
    return HttpResponse(documento)
def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    #doc_fecha = open("C:/Users/ramnd/Desktop/curso-django-pildoras-info/project1/project1/templates/fecha.html")
    #plt_fecha = Template(doc_fecha.read())
    #doc_fecha.close()
    #ctx_fecha = Context({"fecha_ahora": fecha_actual})
    #documento = plt_fecha.render(ctx_fecha)
    #return HttpResponse(documento)
    return render(request, "fecha.html", {"fecha_ahora": fecha_actual})
def calculaEdad(request, nacim, agno):
    edadActual = nacim
    periodo = agno - 2021
    edadFutura = edadActual + periodo
    doc_edad = open("C:/Users/ramnd/Desktop/curso-django-pildoras-info/project1/project1/templates/edad.html")
    plt_edad = Template(doc_edad.read())
    doc_edad.close()
    ctx_edad = Context({"edad_actual": edadActual, "edad_futura": edadFutura})
    documento = plt_edad.render(ctx_edad)
    return HttpResponse(documento)
def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "home.html", {"fecha_ahora": fecha_actual})
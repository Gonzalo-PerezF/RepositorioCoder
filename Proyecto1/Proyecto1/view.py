
from datetime import date, datetime
from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context #para que funcione Template
from django.template import loader


def saludo(request): #Nuestra primera vista :)
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request): #Nuestra segunda vista :)
    return HttpResponse('<br><br>Ya entendí esto')

def buta(request): #Nuestra segunda vista :)
    return HttpResponse('<br><br>Butaa es alto gato!!!!')

#def dia_de_hoy

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def tercera_vista(request, edad): #En que año nací
    fecha_actual = date.today()
    anio = fecha_actual.year #para q me de el año en años
    edad = int(edad) #En fecha iría nuestra edad
    resultado = anio - edad
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)

# def probandoTemplate(self):
#     miHtml=open(r'C:\Users\Flaco\Desktop\Python\PythonProyect\Django\Proyecto1\Proyecto1\plantillas\template1.html') #boton sec y Copiar ruta de acceso
#     plantilla=Template(miHtml.read()) #se carga en la memoria nuestro doc temporal
#     miHtml.close() #cerramos l archivo
#     miContexto=Context() #se crea para los parametros
#     documento=plantilla.render(miContexto) #Renderizamos la plantilla en documento

#     return HttpResponse(documento)

def probandoTemplate(request):
    nom='Gonzalo'
    ap='PerezF'
    lista_notas=[2,2,3,7,2,5]
    diccionario={'nombre':nom,'apellido':ap,'notas':lista_notas}

    plantilla=loader.get_template('template1.html') #en estas 2 lineas soluciono varias de lo anterior
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)

def pruebaT(request):
    nombre='Gonzalo'
    oficio='Doctor'
    nuevo_dic={'nombre':nombre,'oficio':oficio}
    nueva_plantilla=loader.get_template('template3.html')

    documento=nueva_plantilla.render(nuevo_dic)

    return HttpResponse(documento)
    




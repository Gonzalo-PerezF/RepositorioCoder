from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Familiar

# Create your views here.
def familia(self):

    familiar1=Familiar(nom='Ruben',ap='Pérez',edad='65',nacimiento='1957-5-7',relacion='Padre')
    familiar1.save()

    familiar2=Familiar(nom='Nilda',ap='Fernandez',edad='68',nacimiento='1955-8-25',relacion='Madre')
    familiar2.save()

    familiar3=Familiar(nom='Lucas',ap='Buttafouco',edad='29',nacimiento='1992-7-7',relacion='Hermano')
    familiar3.save()

    documento= f'El es {familiar1.nom} {familiar1.ap} tiene {familiar1.edad} ya que nació el {familiar1.nacimiento} y es mi {familiar1.relacion}.\n \nElla es {familiar2.nom} {familiar2.ap} tiene {familiar2.edad} ya que nació el {familiar2.nacimiento} y es mi {familiar2.relacion}. \n El es {familiar3.nom} {familiar3.ap} tiene {familiar3.edad} ya que nació el {familiar3.nacimiento} y es mi {familiar3.relacion}'
    #error no puedo bajar el renglon
    
    return HttpResponse(documento) #mando un template muy simple
    
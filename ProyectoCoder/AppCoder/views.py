from datetime import datetime


from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.thon manage.py migrate

def curso(self):  
    curso = Curso(nombre= "Programación", comision = "8354")
    curso.save()
    documento = f"El curso es : {curso.nombre}, la comision: {curso.comision}"
    
    return HttpResponse(documento)

# def estudiantes(self):
#     estudiante2 = Estudiante(nombre= "El Pepe", apellido = "PorMexico")
#     curso.save()
#     documento = f"El estudiante es : {estudiante2.nombre}, el apellido es: {estudiante2.camada}"
    
#     return HttpResponse(documento)


#-----------------------------Del TP---------------------------- 
# def index(request):
#     return render(request, 'index.html')
# def familiar(request):
#     return render(request, 'familiares.html')
# def familiares(request):
#         familiares = Familia.objects.all()
#         context = {'familiares':familiares}
#         return render(request, 'familiares.html', context=context)
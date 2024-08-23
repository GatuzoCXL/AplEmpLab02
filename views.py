from django.shortcuts import render
import math

def formulario(request):
    return render(request, 'encuesta/formulario.html')

def respuesta(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        edad = request.POST.get('edad', '')
        context = {'nombre': nombre, 'edad': edad}
        return render(request, 'encuesta/respuesta.html', context)
    return render(request, 'encuesta/formulario.html')

#-_-___---__-_____--___---___-____
#funcones añadidas
def tarea(request):
    return render(request, 'encuesta/tarea.html')

def resultado(request):
    if request.method == 'POST':
        num1 = float(request.POST['numero1'])
        num2 = float(request.POST['numero2'])
        operacion = request.POST['operacion']
        
        if operacion == 'suma':
            resultado = f"La suma de {num1} + {num2} = {num1 + num2}"
        elif operacion == 'resta':
            resultado = f"La resta de {num1} - {num2} = {num1 - num2}"
        elif operacion == 'multiplicacion':
            resultado = f"La multiplicación de {num1} * {num2} = {num1 * num2}"
        
        return render(request, 'encuesta/resultado.html', {'resultado': resultado})
    return render(request, 'encuesta/tarea.html')

def cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def volumen_cilindro(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = math.pi * (radio ** 2) * altura
        resultado = f"El volumen del cilindro es {volumen:.2f} metros cúbicos"
        return render(request, 'encuesta/resultado.html', {'resultado': resultado})
    return render(request, 'encuesta/cilindro.html')
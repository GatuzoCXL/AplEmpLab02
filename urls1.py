from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('respuesta/', views.respuesta, name='respuesta'),
    path('tarea/', views.tarea, name='tarea'),#ruta añadida
    path('resultado/', views.resultado, name='resultado'),#ruta añadida
    path('cilindro/', views.cilindro, name='cilindro'),#ruta añadida
    path('volumen-cilindro/', views.volumen_cilindro, name='volumen_cilindro'),#ruta añadida
]




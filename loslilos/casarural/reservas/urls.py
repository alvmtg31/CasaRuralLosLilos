
from django.urls import path
from .views import home, la_casa, reservas, entorno, contacto 
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('la_casa/', la_casa, name='la_casa'),
    path('reservas/', reservas, name='reservas'),
    path('entorno/', entorno, name='entorno'),
    path('contacto/', contacto, name='contacto'),
    path('gotor/', views.gotor, name='gotor'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('actividades/', views.actividades, name='actividades'),
    
    
]


from django.urls import path
from .views import home, la_casa, reservar, entorno, contacto
from . import views
from .views import reservar


urlpatterns = [
    path('', home, name='home'),
    path('la_casa/', la_casa, name='la_casa'),
    path('reservas/', reservar, name='reservas'),
    path('entorno/', entorno, name='entorno'),
    path('contacto/', contacto, name='contacto'),
    path('gotor/', views.gotor, name='gotor'),
    path('gastronomia/', views.gastronomia, name='gastronomia'),
    path('actividades/', views.actividades, name='actividades'),
]

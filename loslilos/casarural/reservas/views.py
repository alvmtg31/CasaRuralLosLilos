from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import request
from django.core.mail import send_mail
from .models import Reserva, Cliente
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import Contacto
from django.contrib.auth import logout
from django.views.generic import ListView
from django import forms





def home(request):
    return render(request, 'reservas/home.html')

def la_casa(request):
    return render(request, 'reservas/la_casa.html')


def reservar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        personas = request.POST.get('personas')
        comentario = request.POST.get('comentario')
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')

        # Calcular el número de noches
        if fecha_entrada and fecha_salida:
            fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d')
            fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d')
            diferencia_dias = (fecha_salida - fecha_entrada).days
            if diferencia_dias > 0:
                precio_total = diferencia_dias * 70
            else:
                precio_total = 0
        else:
            precio_total = 0

        # Construir el mensaje del correo electrónico
        asunto = 'Confirmación de Reserva - Casa Rural'
        mensaje = f"""
        Hola {nombre} {apellidos},

        Gracias por hacer una reserva con nosotros. Aquí están los detalles de tu reserva:

        Nombre: {nombre} {apellidos}
        Email: {email}
        Teléfono: {telefono}
        Dirección: {direccion}
        Número de personas: {personas}
        Fecha de entrada: {fecha_entrada.date()}
        Fecha de salida: {fecha_salida.date()}
        Comentario adicional: {comentario}
        Precio total: {precio_total:.2f} euros

        El pago se realizará en efectivo en el alojamiento.

        ¡Esperamos verte pronto!

        Saludos,
        Casa Rural Los Lilos
        """
        from_email = 'tu_email@dominio.com'  # Reemplaza con tu dirección de correo electrónico
        to_email = email  # Dirección del destinatario

        # Configura el backend del correo electrónico
        send_mail(asunto, mensaje, from_email, [to_email])

        # Redirigir a una página de confirmación
        return render(request, 'reservas/reserva_confirmada.html', {'nombre': nombre, 'precio_total': precio_total})

    return render(request, 'reservas/reservas.html')

def entorno(request):
    return render(request, 'reservas/entorno.html')

def contacto(request):
    if request.method == 'POST':
        form = Contacto(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            send_mail(asunto, mensaje, email, ['loslilosgotor@gmail.com', email])
            return render(request, 'reservas/envioOK.html', {'nombre': nombre})
        # Si el formulario no es válido, volver a renderizar la página de contacto con el formulario y los errores
        return render(request, 'reservas/contacto.html', {'form': form})
    
    # Si la solicitud no es POST, simplemente renderizar la página de contacto con el formulario vacío
    form = Contacto()
    return render(request, 'reservas/contacto.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

def gotor(request):
    return render(request, 'reservas/gotor.html')

def actividades(request):
    return render(request, 'reservas/actividades.html')

def gastronomia(request):
    return render(request, 'reservas/gastronomia.html')

def lista_reservas(request):
    reservas = Reserva.objects.all()  # Obtener todas las reservas
    print(reservas)  # Agregar esta línea para depurar
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})




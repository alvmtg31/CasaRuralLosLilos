from datetime import datetime
from django.conf import settings
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


from django.core.mail import send_mail
from django.shortcuts import render
from datetime import datetime
from .models import Reserva

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

        # Crear o recuperar el cliente
        cliente, created = Cliente.objects.get_or_create(
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono,
            direccion=direccion,
            comentario_cliente=comentario
        )

        # Verificar si la fecha está disponible
        reservas_existentes = Reserva.objects.filter(
            fecha_inicio__lt=fecha_salida,
            fecha_fin__gt=fecha_entrada
        )

        if reservas_existentes.exists():
            # Mostrar mensaje de disponibilidad
            return render(request, 'reservas/reservas.html', {'error': 'La casa está reservada para las fechas seleccionadas.'})

        # Calcular el precio
        fecha_entrada = datetime.strptime(fecha_entrada, '%Y-%m-%d').date()
        fecha_salida = datetime.strptime(fecha_salida, '%Y-%m-%d').date()
        diferencia_dias = (fecha_salida - fecha_entrada).days
        precio_total = diferencia_dias * 70

        # Crear la reserva
        reserva = Reserva.objects.create(
            cliente=cliente,
            personas=personas,
            fecha_inicio=fecha_entrada,
            fecha_fin=fecha_salida,
            precio_total=precio_total,
            comentario=comentario
        )

        # Enviar el correo de confirmación
        subject = 'Confirmación de Reserva'
        message = f'''
        Estimado {nombre} {apellidos},

        Su reserva ha sido confirmada con éxito.

        Fechas de la reserva:
        - Fecha de entrada: {fecha_entrada}
        - Fecha de salida: {fecha_salida}
        
        Número de personas: {personas}
        Precio total: {precio_total} euros

        Comentario adicional: {comentario}

        Gracias por elegir nuestra casa rural.

        Saludos,
        El equipo de Casa Rural
        '''
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        # Redireccionar a la página de confirmación
        return redirect('reserva_confirmada')

    return render(request, 'reservas/reservas.html')

def reserva_confirmada(request):
    return render(request, 'reservas/reserva_confirmada.html')


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




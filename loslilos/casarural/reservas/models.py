from django.db import models
from django.views.generic import TemplateView, FormView
# reservas/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse
from django.utils import timezone

class CasaRural(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.PositiveIntegerField()
    numero_habitaciones = models.PositiveIntegerField(blank=True, null=True)
    numero_banos = models.PositiveIntegerField(blank=True, null=True)
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(max_length=255, blank=True, null=True)
    servicios = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, default='Apellido')
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    personas = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()  # Fecha de entrada
    fecha_fin = models.DateField()     # Fecha de salida
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'Reserva de {self.nombre} {self.apellidos} del {self.fecha_inicio} al {self.fecha_fin}'

class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha_pago = models.DateField(default=timezone.now)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Pago {self.id} - Reserva {self.reserva.id}'

class Disponibilidad(models.Model):
    casa_rural = models.ForeignKey(CasaRural, on_delete=models.CASCADE)
    fecha = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.casa_rural.nombre} - {self.fecha}'

class Comentario(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    casa_rural = models.ForeignKey(CasaRural, on_delete=models.CASCADE)
    comentario = models.TextField()
    valoracion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Comentario de {self.cliente} - {self.casa_rural.nombre}'

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_contacto, self.email, self.telefono, self.asunto, self.mensaje
    

    
    



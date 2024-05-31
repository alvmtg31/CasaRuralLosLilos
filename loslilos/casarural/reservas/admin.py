# reservas/admin.py

from django.contrib import admin
from .models import CasaRural, Cliente, Reserva, Pago, Disponibilidad, Comentario

admin.site.register(CasaRural)
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Disponibilidad)
admin.site.register(Comentario)


from django import forms
from .models import Reserva, Cliente, CasaRural

class Contacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=15)
    asunto = forms.CharField(label='Asunto', max_length=100)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)
    
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
         
        
        
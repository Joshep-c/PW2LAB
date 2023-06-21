from django import forms
from .models import Producto

# Clase que funciona como intermediario entre el modelo y el view

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'descripcion', 
            'precio'
        ]

from django.db import models

# Creacion del unico objeto por ahora usado, en este caso solo con tres atributos, simples
class Producto(models.Model):
    # El primer parametro hace referencia a que se esta obligado a llenarlo, ya que no permite valores nulos
    # y el segundo la maxima cantidad de caracteres
    nombre = models.CharField(null=False, max_length=50)
    descripcion = models.TextField(max_length=500)
    precio = models.DecimalField(max_digits=7, decimal_places=2)


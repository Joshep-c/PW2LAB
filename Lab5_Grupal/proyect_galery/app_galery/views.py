from django.shortcuts import render
from .forms import ProductoForm

# Importamos para obtener la informacion de la base de datos
from .models import Producto


# Create your views here.

def form_add_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    else:
        form = ProductoForm()
    return render(request, 'add-producto.html', {'form': form})

def galeria(request):
    # La parte de objects.all() es un metodo para extraer toda la info de la base de datos que contenga esa clase
    productos = Producto.objects.all()
    return render(request, "galery-productos.html", {"productos": productos})

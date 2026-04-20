from django.shortcuts import render
from .models import Producto # Asegurate de importar tu modelo

def index(request):
    productos = Producto.objects.all() # Trae todos los productos de la DB
    return render(request, 'index.html', {'productos': productos})
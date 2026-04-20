from django.contrib import admin
from .models import Cliente, Domicilio, Producto

class DomicilioInline(admin.TabularInline):
    model = Domicilio
    extra = 1  # Número de filas vacías para agregar nuevos

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'mail')
    search_fields = ('apellido', 'mail')
    inlines = [DomicilioInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    list_filter = ('precio',)
    search_fields = ('nombre',)

# Si prefieres gestionar domicilios por separado también:
@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'cliente')
    list_filter = ('codigo_postal',)
from django.contrib import admin
from django.contrib.auth.models import User
from .models import DatosUsuario, Domicilio, Producto


class DatosUsuarioInline(admin.StackedInline):
    model = DatosUsuario
    extra = 0


class DomicilioInline(admin.TabularInline):
    model = Domicilio
    extra = 1


class UserAdminExtendido(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    inlines = [DatosUsuarioInline, DomicilioInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    list_filter = ('precio',)
    search_fields = ('nombre',)


@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'user', 'codigo_postal')
    list_filter = ('codigo_postal',)


admin.site.unregister(User)
admin.site.register(User, UserAdminExtendido)
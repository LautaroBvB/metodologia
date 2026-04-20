from django.db import models
from django.contrib.auth.models import User

class DatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Domicilio(models.Model):
    calle = models.CharField(max_length=200)
    numero = models.IntegerField()
    departamento = models.CharField(max_length=50, null=True, blank=True)
    codigo_postal = models.CharField(max_length=20)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='domicilios')

    def __str__(self):
        return f"{self.calle} {self.numero}"

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    # Nuevo campo de descripción
    descripcion = models.TextField(blank=True, null=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
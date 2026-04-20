from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Domicilio(models.Model):
    calle = models.CharField(max_length=200)
    numero = models.IntegerField()
    # null=True permite nulos en DB, blank=True permite vacío en formularios
    departamento = models.CharField(max_length=50, null=True, blank=True)
    codigo_postal = models.CharField(max_length=20)
    
    # Relación muchos a uno (un cliente, varios domicilios)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='domicilios')

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
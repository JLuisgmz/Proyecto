from django.db import models

# Create your models here.

class UsuarioN(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    dpi = models.CharField(max_length=20, null=False)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15, null=False)
    nombre_usuario = models.CharField(max_length=50, null=False)
    correo_electronico = models.EmailField(max_length=254, null=False)
    contraseña = models.CharField(max_length=100, null=False)
    confirmacion_contraseña = models.CharField(max_length=100, null=False)

class UsuarioE(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    dpi = models.CharField(max_length=20, null=False)
    usuario = models.CharField(max_length=100, default='valor_predeterminado')
    contraseña = models.CharField(max_length=100, null=False)
    confirmacion_contraseña = models.CharField(max_length=100, null=False)
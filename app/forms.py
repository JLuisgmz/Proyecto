from django import forms
from .models import UsuarioN

class UsuarioNForm(forms.ModelForm):
    class Meta:
        model = UsuarioN
        fields = ['nombre', 'apellido', 'dpi', 'fecha_nacimiento', 'telefono', 'nombre_usuario', 'correo_electronico', 'contraseña', 'confirmacion_contraseña']
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class profile(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(blank=True,upload_to='photos')
    bio = models.TextField
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"



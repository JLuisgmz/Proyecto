from django.db import models

# Create your models here.
from profiles.models import profile

class log(models.Model):
    profile=models.ForeignKey(profile,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"log de {self.profile}"
from django.db import models

from django.contrib.auth.models import User

from Herramientas.get_dir_gera import get_direccion_gera

class Empleado(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    nombre_completo= models.CharField(max_length=200)
    puesto = models.CharField(max_length=100)
    fecha_registro =models.DateTimeField(auto_now_add=True)

class Direccion(models.Model):
    empleado= models.ForeignKey(Empleado,on_delete=models.CASCADE)
    latitud=models.CharField(max_length=20)
    longitud= models.CharField(max_length=20)
    direccion_completa =models.CharField(max_length=300,blank=True, null=True)
    fecha_registro= models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.direccion_completa=get_direccion_gera(self.latitud,self.longitud)
        super().save(*args, **kwargs)

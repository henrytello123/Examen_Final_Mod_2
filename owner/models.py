from django.db import models

class Owner(models.Model):
   nombre = models.CharField(max_length=40)
   edad = models.CharField(max_length=5, default='')
   pais = models.CharField(max_length=30, default='')

def __str__(self):
   return "{} tiene {} años".format(self.Nombre, self.Edad)


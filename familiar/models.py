from django.db import models



class Person(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    apellido = models.CharField("Apellido", max_length=30)
    GENERO = (
        (1,"Maculino"),
        (2,"Femenino"),
        (3,"Otro"),
    )
    genero = models.PositiveSmallIntegerField(choices= GENERO)
    edad = models.PositiveIntegerField("Edad")
    correo = models.EmailField("Correo")
    fecha = models.CharField("Cumpleaños", max_length=15)

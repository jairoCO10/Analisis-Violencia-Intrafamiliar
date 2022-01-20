from django.db import models

# Create your models here.

class violencia(models.Model):
    Departamento = models.CharField(max_length=100)
    Municipio = models.CharField(max_length=100)
    CodigoDane = models.CharField(max_length=100)
    ArmasMedios = models.CharField(max_length=100)
    FechaHecho = models.DateField()
    MASCULINO = 'MA'
    FEMENINO = 'FE'
    GeneroChoices =[
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    Genero = models.CharField(max_length=2, choices=GeneroChoices, default=MASCULINO,)
    GrupoEtario = models.CharField(max_length=100)
    Cantidad = models.IntegerField()
    
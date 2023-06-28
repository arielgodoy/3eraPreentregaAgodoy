from django.db import models

# Create your models here.

class Documento(models.Model):
    titulo = models.CharField(db_column='titulo', max_length=100, blank=False)
    descripcion = models.CharField(db_column='descripcion', max_length=100, blank=False)
    autor = models.CharField(db_column='autor', max_length=100, blank=False)
    anio = models.IntegerField(db_column='anio',blank=False, default=2000)
from django.db import models


class Medico(models.Model):
    id_Medico = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    def __str__(self) -> str:
        return super().__str__()

class Paciente(models.Model):
    id_paciente = models.IntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateTimeField()
    sexo = models.CharField(max_length=10)
    altura = models.FloatField()
    medicoid = models.ForeignKey(Medico, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()
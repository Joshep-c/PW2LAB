from django.db import models

class Docente(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Estudiante(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Asignatura(models.Model):
    name = models.CharField(max_length=50)
    docentes = models.ManyToManyField(Docente)

    def __str__(self):
        return self.name

class Delegado(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.estudiante.name} - {self.asignatura.name}"

    class Meta:
        unique_together = ('asignatura',)

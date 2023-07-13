from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Docente)
admin.site.register(Asignatura)
admin.site.register(Estudiante)
admin.site.register(Delegado)

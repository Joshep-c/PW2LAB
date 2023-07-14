from django.urls import path
from .import views

urlpatterns = [
    path('',views.tabla_asignaturas,name="index"),
]
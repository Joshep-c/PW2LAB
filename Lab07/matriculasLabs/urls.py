from django.urls import path
from .import views

urlpatterns = [
    path('',views.tabla_asignaturas,name="index"),
    path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
]
from django.urls import path
from .import views

urlpatterns = [
    path('',views.tabla_asignaturas,name="index"),
    path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
    path('send-email/', views.send_email, name='send_email'),
]
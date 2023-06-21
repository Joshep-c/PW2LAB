from django.urls import path
from . import views

# urls para poder acceder a las dos paginas, Ejml: http://127.0.0.1:8000/galeria/ puedes obviar el '/' final
urlpatterns = [
    path('productos/', views.form_add_productos, name="productos"),
    path('galeria/', views.galeria, name="galeria"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
]

from django.shortcuts import render
from django.http import HttpResponse

def lista_usuarios(request):
    return HttpResponse("Lista de usuários")

def cadastro_usuario(request):
    return HttpResponse("Página de cadastro de usuário")

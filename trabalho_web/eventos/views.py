from django.shortcuts import render
from django.http import HttpResponse

def lista_eventos(request):
    return HttpResponse("Lista de eventos")

def cadastro_evento(request):
    return HttpResponse("Página de cadastro de evento")



from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):

    return HttpResponse ("Inicio")

def matriz(request):

    return HttpResponse ("Matriz")

def historico(request):

    return HttpResponse ("Historico")
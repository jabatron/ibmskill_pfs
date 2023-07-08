from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):

    return render(request, "matriz/base.html")

def matriz(request):

    return render(request, "matriz/inicio.html")

    return render(request, "matriz/matriz.html")

def historico(request):

    return render(request, "matriz/historico.html")

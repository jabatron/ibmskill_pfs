from django.shortcuts import render, HttpResponse

try:
    import matriz.matriz as mm
except:
    print ("se ha producido un error al importar")

# Create your views here.


def home(request):

    return render(request, "matriz/inicio.html")

def matriz(request):
    matriz, suma_columna, suma_fila = mm.generar_matriz(4,4)

    for f, sf in enumerate (suma_fila):
        matriz[f].append('>')
        matriz[f].append(sf)
    
    matriz.append(['v'] * (len(matriz[0])-2))
    matriz.append(suma_columna)


    md = {
        "m": matriz,
    }

    print (md)
    return render(request, "matriz/matriz.html", context=md)

def historico(request):

    return render(request, "matriz/historico.html")

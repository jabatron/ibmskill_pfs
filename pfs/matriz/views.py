from django.shortcuts import render, HttpResponse

from .forms import DimensionForm

try:
    import matriz.matriz as mm
except:
    print ("se ha producido un error al importar")

# Create your views here.


def home(request):

    return render(request, "matriz/inicio.html")

def matriz(request):

    if request.method == 'POST':
        form = DimensionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['dimension']
            print (data)
            matriz, suma_columna, suma_fila = mm.generar_matriz(data,data)

            for f, sf in enumerate (suma_fila):
                matriz[f].append('>')
                matriz[f].append(sf)
            
            matriz.append(['v'] * (len(matriz[0])-2))
            matriz.append(suma_columna)
            md = {
                "m": matriz,
                "form" : form,
            }

    else: 
        form = DimensionForm()
        
        md = {
            "m": "",
            "form" : form,
        }

    return render(request, "matriz/matriz.html", context=md)

def historico(request):

    return render(request, "matriz/historico.html")

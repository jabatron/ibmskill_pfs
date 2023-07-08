import numpy as np
import argparse

# hay que generar una matrix con números de 0 a 9
LIMITE_MINIMO = 0
LIMITE_MAXIMO = 9

def generar_matriz (x, y):
    ''' Genera una matriz aleatoria de X por Y elementos con valores de 0 a 9
        x: int dimension X
        y: int dimension Y

        Devuelve
        matriz -> matriz aleatoria generada, es una lista de listas
        suma_columnas_matriz -> lista con la suma de las columnas
        suma_filas_matriz -> lista con la suma de las filas
    '''

    # genera una matrix de x filas por y columnas con números aleatorios entre limite minimo y máximo
    matriz = np.random.randint(LIMITE_MINIMO, LIMITE_MAXIMO, (x,y))

    # genera una lista con la suma de las columnas
    suma_columnas_matriz = matriz.sum(axis=0)
    # genera una lista con la suma de las filas
    suma_filas_matriz    = matriz.sum(axis=1)

    # Devuelve una tupla con la matrix, una lista con la suma de las columnas y otra lista con la suma de las filas
    return list(matriz), list(suma_columnas_matriz), list(suma_filas_matriz)

def generar_matriz_con_sumas(x, y):
    # genera una matrix de x filas por y columnas con números aleatorios entre limite minimo y máximo
    matriz_inicial = np.random.randint(LIMITE_MINIMO, LIMITE_MAXIMO, (x,y))

    # genera una lista con la suma de las columnas
    suma_columnas_matriz = matriz_inicial.sum(axis=0)
    # genera una lista con la suma de las filas
    suma_filas_matriz    = matriz_inicial.sum(axis=1)

    matriz_suma_columnas = np.append(matriz_inicial, [suma_columnas_matriz], axis=0)

    matriz_suma_filas = [[e] for e in suma_filas_matriz]
    #añadir un 0 en la interseción de filas y columnas.
    matriz_suma_filas.append([0])
    matriz_final = np.append(matriz_suma_columnas, matriz_suma_filas, axis=1)

    return matriz_final.tolist()



#cuando usemos "matriz.py" como módulo en django no importará lo que viene a continuación
if __name__ == '__main__':

    # valida que el argumento que le pasamos por línea de comandos sea un entero entre 1 y 30
    def valid_int(i):
        try:
            num = int(i)
            if num > 0 and num < 31:
                return num
            else:
                raise 

        except:
            raise argparse.ArgumentTypeError('Escriba un numero de entre 1 y 30')

    # Permitimos introducir la dimensión de la matriz en la línea de comandos
    parser = argparse.ArgumentParser(description='Generación de matriz aleatorio de NxN y suma de filas y columnas.')
    parser.add_argument('-d', '--dimension', metavar='dimension', type=valid_int, help='Dimension de la matriz')

    # Detectar si pasamos la dimensión de la matriz como argumento.
    args = parser.parse_args()

    # Verificamos si se ha introducido la dimensión de la matriz como argumento
    if not args.dimension:
        # Vigilar que se ha introducido un número entero
        fin = False
        # Realiza un bucle hasta que introducimos un entero valido (entre 1 y 30)
        while not fin:
            try:
                dimension = int (input ("Introduzca el valor de la dimension (1-30): "))
                if dimension > 0 and dimension < 31:
                    fin = True
                else:
                    #Provocamos una excepción ya que el valor no es el adecuado
                    raise
            except:
                #Si el número no es un entero se provoca una excepción
                print ("El numero introducido no es un entero en el rango 1-30")
                fin = False

    else:
        dimension = args.dimension

    # Usamos la funcion para generar la matriz y las sumas
    matriz_aleatoria, suma_columnas, suma_filas = generar_matriz(dimension, dimension)

    # Pintamos en pantalla la matriz, y la suma de filas
    print (f'Matriz de dimension {dimension} x {dimension}. Con suma de columanas y filas.')
    for i, fila in enumerate(matriz_aleatoria):
        for j in fila:
            print (f'{j:4}', end=' ')
        print (f' -> {suma_filas[i]:4}')

    print ('-' * 5 * dimension)

    # Finalmente pintamos la suma de columnas
    for j in suma_columnas:
        print (f'{j:4}', end=' ')
    print('')

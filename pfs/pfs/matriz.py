import numpy as np
import argparse

# hay que generar una matrix con números de 0 a 9
LIMITE_MINIMO = 0
LIMITE_MAXIMO = 9

def generar_matriz (x, y):

    # genera una matrix de x filas por y columnas con números aleatorios entre limite minimo y máximo
    matriz_inicial = np.random.randint(LIMITE_MINIMO, LIMITE_MAXIMO, (x,y))

    # genera una lista con la suma de las columnas
    suma_columnas_matriz = matriz_inicial.sum(axis=0)
    # genera una lista con la suma de las filas
    suma_filas_matriz    = matriz_inicial.sum(axis=1)

    # Devuelve una tupla con la matrix, una lista con la suma de las columnas y otra lista con la suma de las filas
    return matriz_inicial, suma_columnas_matriz, suma_filas_matriz

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


if __name__ == '__main__':

    def valid_int(i):
        try:
            num = int(i)
            if num > 0 and num < 31:
                return num
            else:
                raise 

        except:
            raise argparse.ArgumentTypeError('Escriba un numero de entre 1 y 30')



    parser = argparse.ArgumentParser(description='Generación de matriz aleatorio de NxN y suma de filas y columnas.')
    parser.add_argument('-d', '--dimension', metavar='dimension', type=valid_int, help='Dimension de la matriz')

    args = parser.parse_args()
    
    matriz_aleatoria, suma_columnas, suma_filas = generar_matriz(args.dimension, args.dimension)
    for i, fila in enumerate(matriz_aleatoria):
        for j in fila:
            print (f'{j:4}', end=' ')
        print (f' -> {suma_filas[i]:4}')

    print ('-' * 5 * args.dimension)

    for j in suma_columnas:
        print (f'{j:4}', end=' ')
    print('')

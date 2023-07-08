from matriz import generar_matriz
import unittest

class TestMatriz(unittest.TestCase):
    def setUp (self):
        # Genero una matriz y calculo las sumas
        self.dimension = 4
        self.matriz, self.sc, self.sf = generar_matriz(self.dimension, self.dimension)
        
    def test_suma_columnas(self):
        suma_columnas = [0] * self.dimension
        #Ahora calculo la suma por otro metodo, recorriendo filas y columnas
        for filas in self.matriz:
            for i, c in enumerate(filas):
                suma_columnas[i] += c

        self.assertEqual(self.sc, suma_columnas, "Las columnas no suman lo mismo")

    def test_suma_filas(self):
        suma_filas = [0] * self.dimension
        #Ahora calculo la suma por otro metodo, recorriendo filas y columnas
        for i, filas in enumerate(self.matriz):
            for c in filas:
                suma_filas[i] += c

        self.assertEqual(self.sf, suma_filas, "Las filas no suman lo mismo")



if __name__ == "__main__":
    unittest.main()

"""
Nombre: Cilindro.py
Objetivo: Es la subclase de Circunferencia
Autor: Lucio David Morán B
Fecha: 09 de noviembre de 2019
"""
from Punto import Punto
from Circunferencia import Circunferencia

class Cilindro(Circunferencia):
    #Método constructor
    def __init__(self, valorX, valorY, vradio, valtura):
        #Actualizamos atributos del cilindro
        self.altura = valtura
        #Actualizamos las
        Circunferencia.__init__(self, vradio, valorX, valorY)
        Punto.__init__(self, valorX, valorY)
    
    #Método get de Altura
    def getAltura(self):
        return self.altura
    
    #Método set de ALtura
    def setAltura(self, valtura):
        self.altura = valtura
    
    #Método toString
    def toString(self):
        return "La altura del cilindro es: ",str(self.altura)
    
    
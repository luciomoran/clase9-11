"""
Nombre: Punto.py
Objetivo: Es la superclase en la jerarquía de herencia.
Autor: Lucio David Morán B
Fecha: 09 de noviembre de 2019
"""
from Punto import Punto

class Circunferencia(Punto):
    #Método constructor
    def __init__(self, valorX, valorY, vradio):
        #Actualizar el atributo
        self.radio = vradio
        #Actualizar los atributos de Punto
        Punto.__init__(self, valorX, valorY)

    #Lista de métodos get 
    def getRadio(self):
        return self.radio

    #Lista de métodos set para el radio 
    def setRadio(self, vradio):
        self.radio = vradio

    #Métodos toString
    def toString(self):
        return "El valor de radio es: ",str(self.radio)
    
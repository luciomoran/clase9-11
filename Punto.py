"""
Nombre: Punto.py
Objetivo: Es la superclase en la jerarquía de herencia.
Autor: Lucio David Morán B
Fecha: 09 de noviembre de 2019
"""

class Punto(object):
    #Método constructor
    def __init__(self, valorX, valorY):
        #Creamos los atributos
        self.x = valorX
        self.y = valorY

    #Lista de métodos get
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    #Lista de métodos set
    def setX(self, valorX):
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY
    
    #Método toString()
    def toString(self):
        return "Las coordenadas del punto son: ",str(self.x),", ",str(self.y)
        
    
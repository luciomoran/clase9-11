"""
Nombre: Cilindro.py
Objetivo: Instanciar a la clase cilindro
Autor: Lucio David Morán B
Fecha: 09 de noviembre de 2019
"""
from Cilindro import Cilindro
from tkinter import *

def main():
    #Creamos ventana raíz
    w = Tk()
    #Atributos
    w.title("Objetos tipo Cilindro")
    w.geometry("500x500")

    lbl = Label(w, text="Coordenadas en X: ")
    lbl.grid(column=5, row=5)
    lbl = Label(w, text="Coordenada en Y: ")
    lbl.grid(column=5, row=8)

    #Creamos un objeto de la clase Cilindro
    cil = Cilindro(10,10,12.13,25.11)
    
    #Hacer un ciclo loop para que la ventana quede visible
    w.mainloop()

if __name__=="__main__":
    main()


"""
Nombre: CRUD.py
Objetivo: Menú CRUD con operaciones
Autor: Lucio David Morán B
Fecha: 13 de noviembre de 2019
"""
import mysql.connector

mydb = ""

#Abre la conexión con la base de datos
def abrirConexionDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="mibase",
        passwd=""
    )
    print(mydb)


def insertarRegistro():
    print("Introduce los campos para insertar un Trabajador")
    #Solicitamos los campos
    clave = input("Introduce la clave del trabajador:")
    nombre = input("Introduce nombre del trabajador:")
    salary = input("Introduce sueldo del trabajador:")

    mycursor = mydb.cursor()
    sql = "INSERT INTO trbajadores (code, nombre, sueldo) VALUES (clave, nombre, salary)"
    #Ejecutamos sentencia sql
    mycursor.execute(sql)
    val = ("John","Highway 21")
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowCount, "Trabajador insertado...")

def buscarRegistro():
    print()

def cambiarRegistros():
    print()

def borrarRegistros():
    print()

def listaRegistros():
    print()

def dashboard():
    ciclo = "S"
    while ciclo == "S" or ciclo == "s":
        print("---CRUD con MySQL--")
        print("1.- Insertar registros")
        print("2.- Buscar registros")
        print("3.- Cambiar registros")
        print("4.- Borrar registros")
        print("5.- Lista de regsistros")
        print("6. Salir")
        print("\n")
        ciclo = input("Seleccione una opcion entre 1 y 6")

        if ciclo == 1:
            insertarRegistro()
        elif ciclo == 2:
            buscarRegistro()
        elif ciclo == 3:
            cambiarRegistros()
        elif ciclo == 4:
            borrarRegistros()
        elif ciclo == 5:
            listaRegistros()
    #Else del while
    else:
        print("Por favor introduce un número entero")


def main():
    dashboard()


if __name__ == "__main__":
    main()
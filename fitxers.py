#modulo de almacen de los diccionarios que vamos a usar ,habitaciones y reservas

import os
nombre_carpeta="./dades"
ruta_archivo=nombre_carpeta+"/habitacions.txt"
ruta_archivo2=nombre_carpeta+"/reserves.txt"

#funcion principal para crear la carpeta si no existe

def carpeta():
    # Primero verifica si la carpeta existe, si no, la crea
    if not os.path.exists(nombre_carpeta):
        os.mkdir(nombre_carpeta)
        #print("Se creó la carpeta")




#funcion pare leer las habitaciones en el fichero y devolver un diccionario habitaciones para trabajar con el


def leer_habitaciones():

    habitaciones = {}
    # miramos si existe el fichero de datos
    if os.path.exists(ruta_archivo):

        f = open(ruta_archivo, "r")

        lineas = f.readlines()

        f.close()
        habitaciones = {}
        for linea in lineas:
            linea = linea.replace("\n", "")
            linea = linea.split(",")
            numero_habitacion = linea[0]
            capacidad = linea[1]
            precio = linea[2]

            estado = linea[3]
            habitaciones[numero_habitacion] = {
                "capacidad": capacidad,
                "precio": precio,
                "estado": estado,
            }

    return habitaciones






#misma funcion para leer las reservas en el fichero y convertirlas a un diccionario reservas
def leer_reserves():

        reserves = {}
        # miramos si existe el fichero de datos
        if os.path.exists(ruta_archivo2):
            # abrimos para leemos los datos
            f = open(ruta_archivo2, "r")

            lineas2 = f.readlines()

            f.close()

            for linea in lineas2:
                #linea.replace("\n", "")
                lineafitxers = linea.split(",")
                n_habitaciones = lineafitxers[0]
                nombre = lineafitxers[1]
                apellido = lineafitxers[2]
                dni = lineafitxers[3]
                telefono = lineafitxers[4][:-1]

                reserves[n_habitaciones] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "dni": dni,
                    "telefono": telefono,

                }

        return reserves



            


#funcion para escribir la habitacion nueva en el fichero
def escribir_habitacion(numero_habitacion,capacidad,precio):
     carpeta()
     estado="Disponible"
     f=open(ruta_archivo,"a")
     f.write(f"{numero_habitacion},{capacidad},{precio},{estado}\n")
     f.close()


#lo mismo pero con reservas
def escribir_reserves(numerohabit,nombre,apellido,dni,telefono):
    carpeta()
    f=open(ruta_archivo2,"a")
    f.write(f"{numerohabit},{nombre},{apellido},{dni},{telefono}\n")
    f.close()

#funcion para modificar en el diccionario  i en el fichero el estado sobrescribiendo de la habitacion

def sobrescribir_habitaciones(dicc):
        f=open(ruta_archivo, "w")
        for hab in dicc:
            capacidad =dicc[hab]["capacidad"]
            precio = dicc[hab]["precio"]
            estado = dicc[hab]["estado"]
            f.write(f"{hab},{capacidad},{precio},{estado}\n")
        f.close()


 #lo mismo con reservas
def sobrescribir_reserves(dicc2):
    f=open(ruta_archivo2, "w")
    for reserva in dicc2:
        nombre = dicc2[reserva]["nombre"]
        apellido = dicc2[reserva]["apellido"]
        dni = dicc2[reserva]["dni"]
        telefono = dicc2[reserva]["telefono"]
        f.write(f"{reserva},{nombre},{apellido},{dni},{telefono}\n")
    f.close()
#modulo principal de llamada a las funciones de resolucion de lo que pide el ejercicio
import biblioteca_datos as biblio
import sys

from fitxers import carpeta


com = [
    "main añadir habitacion -1 4 50",
    "main añadir habitacion 0 1 50",
    "main añadir habitacion 1 0 40",
    "main añadir habitacion aa 1 40",
    "main añadir habitacion 100 aa 50",
    "main añadir habitacion 100 1 -1",
    "main añadir",
    "main añadir habitacion",
    "main añadir reserva",
    "main añadir reserva -1 hornos jordi 123 123",
    "main añadir reserva 0 hornos jordi 123 123",
    "main añadir reserva 100 hornos jordi 123456789 123123123",
    "main añadir reserva 100 hornos jordi 12345678z 123",
    "main finalizar",
    "main finalizar 100 -1",
    "main limpiar",
    "main limpiar 100",
    "main finalizar 100 5",
    "main list",
    "main info 12345678Z",
    "main info asdf asdf",
    "main reservas",
    "main reservas 234",
    "main añadir habitacion 104 4 50",
    "main reservas",
    "main list",
    "main añadir reserva 104 Cabra Loca 12345678z 123456789",
    "main añadir habitacion 105 2 60",
    "main list",
    "main finalizar 100 0",
    "main finalizar 105 4",
    "main añadir habitacion 106 2 40",
    "main añadir reserva 105 Aitor Tilla 11223344t 123456789",
    "main info 12345678z",
    "main info 23415678E",
    "main reservas",
    "main finalizar 104 0",
    "main list",
    "main finalizar 105 4",
    "main list",
    "main limpiar 106",
    "main limpiar 104",
    "main limpiar 105",
    "main list",
]

for c in com:
        argumentos = c.split(" ")

        accion_princial=argumentos[1].lower()

        if accion_princial=="añadir".lower():
            if len(argumentos)>2:
                tipo_accion=argumentos[2].lower()
                if tipo_accion=="habitacion".lower():
                        biblio.afegir_habitacions(argumentos)


                elif tipo_accion=="reserva".lower():
                        biblio.afegir_reserves(argumentos)

                else:
                        print("Accion no valida")


        elif accion_princial=="finalizar".lower():
                biblio.finalizar_habitacion(argumentos)

        elif accion_princial=="limpiar".lower():
                biblio.netejar_habitacion(argumentos)

        elif accion_princial=="list".lower():
                biblio.listar_habitaciones(argumentos)



        elif accion_princial=="reservas".lower():
                biblio.listar_reserves(argumentos)

        elif  accion_princial=="info".lower():
                biblio.listar_dni(argumentos)




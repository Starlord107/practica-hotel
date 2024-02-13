#modulo principal de llamada a las funciones de resolucion de lo que pide el ejercicio
import biblioteca_datos as biblio
import sys

from fitxers import carpeta
if len(sys.argv)<2:
        print("No se ha especificado la accion")

argumentos= sys.argv

accion_princial=argumentos[1].lower()

if accion_princial=="afegir".lower():
        tipo_accion=argumentos[2].lower()
        if tipo_accion=="habitacio".lower():
                biblio.afegir_habitacions(argumentos)


        elif tipo_accion=="reserva".lower():
                biblio.afegir_reserves(argumentos)

        else:
                print("Accion no valida")


elif accion_princial=="finalitzar".lower():
        biblio.finalizar_habitacion(argumentos)

elif accion_princial=="netejar".lower():
        biblio.netejar_habitacion(argumentos)

elif accion_princial=="list".lower():
        biblio.listar_habitaciones(argumentos)



elif accion_princial=="reserves".lower():
        biblio.listar_reserves(argumentos)

elif   accion_princial=="info".lower():
        biblio.listar_dni(argumentos)
        



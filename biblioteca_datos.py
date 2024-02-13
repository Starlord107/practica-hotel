import fitxers as fd
#modulo de funciones que no tienen nada que ver con los ficheros mas bien  otras circustancias

#funcion para comprobar la longitud de caracteres
def comprobar_longitud(argumentos,nu_argumentos):
    iscorrect=True
    if len(argumentos)!=nu_argumentos:
        iscorrect=False

    return iscorrect
#funcion para comprobar que el dni sea valido
def comprobar_dni(dni):
    if len(dni) != 9:
        print("longitud incorrecta")
    else:

        if not dni[:8].isnumeric():
            print("el dni debe tener 8 numeros")
        elif not dni[8].isalpha():
                print("el dni debe tener una letra final")

        else:
            #print("el dni es correcto")
            return dni
#funcion para comprobar que el telefono sea correcto
def  comprobar_telefono(telefono):

    if len(telefono)!=9:
        print("longitud incorrecta")

    else:

        if telefono.isdigit():
            #print("telefono correcto")
            return telefono

        else:
            print("telefono incorrecto")

#aqui empiezan las funciones para realizar las tareas demandadas por el hotel
def afegir_habitacions(argumentos):
    if comprobar_longitud(argumentos,6):
        numero = argumentos[3]
        capacitat = argumentos[4]
        preu = argumentos[5]
        if not numero.isdigit():
            print("la habitacio ha de ser numerica")

        elif int(numero) <=0:
            print("La habitacio no pot ser menor a 0")

        else:
            if fd.leer_habitaciones():
                dicc=fd.leer_habitaciones()
            else:
                dicc={}
            if numero not in dicc:
                fd.escribir_habitacion(numero,capacitat,preu)
                print("habitacio afegida")
        
            else:
                print("aquesta habitacio ya existeix")



    else:
        print("no hi ha el numero correcte arguments")




def afegir_reserves(argumentos):
    if comprobar_longitud(argumentos,8):
        numero_habitacion = argumentos[3]
        nombre_cliente = argumentos[4]
        apellido_cliente = argumentos[5]
        dni_cliente = argumentos[6]
        telefono_cliente = argumentos[7]
        if not numero_habitacion.isdigit():
            print("la habitacio ha de ser numerica")

        elif int(numero_habitacion) <=0:
            print("La habitacio no pot ser menor a 0")
        else:
            dicc = fd.leer_habitaciones()

            if numero_habitacion not in dicc:
                print("aquesta habitacio no existeix")

            else:

                if comprobar_dni(dni_cliente) and comprobar_telefono(telefono_cliente):
                    if fd.leer_reserves():
                        dicc2=fd.leer_reserves()

                    else:
                        dicc2={}

                    if numero_habitacion not in dicc2:
                        if  dicc[numero_habitacion]["estado"]=="Bruta":
                            print("No es pot reservar una habitacio que esta  bruta")
                        else:

                            fd.escribir_reserves(numero_habitacion,nombre_cliente,apellido_cliente,dni_cliente,telefono_cliente)
                            print("reserves afegida")
                            dicc[numero_habitacion]["estado"]="Ocupado"
                            fd.sobrescribir_habitaciones(dicc)
                    else:
                        print("aquesta habitacio ya esta reservada")
    else:
        print("no hi ha el numero correcte arguments")

def finalizar_habitacion(argumentos):
    if comprobar_longitud(argumentos,4):
        numero_habitacion = argumentos[2]
        dias = int(argumentos[3])
        habitaciones=fd.leer_habitaciones()
        if numero_habitacion in habitaciones:


            reservas=fd.leer_reserves()

            if numero_habitacion in reservas:
                if dias >0:
                    dicc_habi=fd.leer_habitaciones()
                    precio=dicc_habi[numero_habitacion]["precio"]
                    precio_total=float(precio)*dias
                    cadena=f"Preu total de l'estada: {precio_total}. L'habitacio queda en espera del servei de neteja"
                    dicc_habi[numero_habitacion]["estado"]="Bruta"
                    fd.sobrescribir_habitaciones(dicc_habi)
                    print(cadena)
                    dicc2=fd.leer_reserves()
                    if numero_habitacion in dicc2:
                        dicc2.pop(numero_habitacion)
                        fd.sobrescribir_reserves(dicc2)
                elif dias==0:
                    dicc_habi2=fd.leer_habitaciones()
                    dicc_reserva=fd.leer_reserves()
                    dicc_habi2[numero_habitacion]["estado"]="Neta"
                    fd.sobrescribir_habitaciones(dicc_habi2)
                    dicc_reserva.pop(numero_habitacion)
                    fd.sobrescribir_reserves(dicc_reserva)
                    print("Reserva anul.lada.Sense cost pel cliente.L'habitacio torna a estar disponible")
                else:
                    print("El numero de dias no pot ser negatiu.Si vols anul.lar la reserva indica numero de dies 0")

            else:
                print("No esta reservada aquesta habitacio")

        else:
            print("aquesta habitacio no existeix")

    else:
        print("no hi ha el numero correcte arguments")


def netejar_habitacion(argumentos):
    if comprobar_longitud(argumentos,3):
        numero_habitacion = argumentos[2]
        habitaciones=fd.leer_habitaciones()
        if numero_habitacion in habitaciones:
            estado_habitaciones=habitaciones[numero_habitacion]["estado"]
            if estado_habitaciones=="Bruta":
                habitaciones[numero_habitacion]["estado"]="Neta"
                print("Habitacio netejada .Queda disponible")
                fd.sobrescribir_habitaciones(habitaciones)
            else:

                print("L'habitacio encara esta ocupada o neta ya no fa falta ")


        else:
            print("aquesta habitacio no existeix")

    else:
        print("no hi ha el numero correcte arguments")



def listar_habitaciones(argumentos):
    if comprobar_longitud(argumentos, 2):
        habitaciones = fd.leer_habitaciones()
        reservas = fd.leer_reserves()
        if not habitaciones:
            print("No hay habitaciones disponibles.")
        else:
            total_habitaciones =0
            Disponibles=0
            ocupades=0
            brutas=0
            print("======== INFO HOTEL  =========")
            print(f"Hab  Cap   Estado")
            for hab in habitaciones:
                numero_habitacion = hab
                capacidad = habitaciones[hab]["capacidad"]
                estado = habitaciones[hab]["estado"]
                total_habitaciones +=1
                info_habitacion =f" {numero_habitacion}  {capacidad}    {estado}"
                if estado=="Bruta":
                    brutas+=1

                elif estado=="Ocupado":
                    ocupades+=1

                elif estado=="Disponible":
                    Disponibles+=1


                if numero_habitacion in reservas:
                    nombre_cliente= reservas[numero_habitacion]["nombre"].title()
                    appelido_cliente = reservas[numero_habitacion]["apellido"].title()

                    info_reserva = f"{info_habitacion} => {nombre_cliente} {appelido_cliente}"



                if estado == "Ocupado":

                    print(info_reserva)
                else:
                    print(info_habitacion)
            print("==============================")
            print(f"Total habitaciones: {total_habitaciones}\nDisponibles: {Disponibles} Ocupades:{ocupades} Brutes:{brutas}")








def listar_reserves(argumentos):
    if comprobar_longitud(argumentos, 2):

        dicc_reservas=fd.leer_reserves()
        if not dicc_reservas:
            print("No hi han reserves disponibles.")

        else:
            for reserva in dicc_reservas:

                nombre_cliente = dicc_reservas[reserva]["nombre"]
                apellido_cliente = dicc_reservas[reserva]["apellido"]
                dni_cliente = dicc_reservas[reserva]["dni"]
                telefono_cliente = dicc_reservas[reserva]["telefono"]
                nombreclinteformato=nombre_cliente.title()+(" ")+apellido_cliente.title()
                info_reserva = f"{reserva}:{dni_cliente}-{nombreclinteformato}-{telefono_cliente}"
                print("=======   RESERVES =========")
                print(info_reserva)




def listar_dni(argumentos):
    if comprobar_longitud(argumentos, 3):
        rev_dni=fd.leer_reserves()

        dni_cliente=argumentos[2]
        if not rev_dni:
            print("No hi han reserves disponibles.")

        else:
            cont = 0
            print("========    RESERVES   =========")

            for reserva in rev_dni:
                dni_biblio= rev_dni[reserva]["dni"].lower()
                nombre_cliente = rev_dni[reserva]["nombre"].title()
                apellido_cliente = rev_dni[reserva]["apellido"].title()
                telefono_cliente = rev_dni[reserva]["telefono"]

                if dni_cliente == dni_biblio:
                    if cont==0:
                        print(f"Dades del client : {apellido_cliente},{nombre_cliente}-Tfn:{telefono_cliente}")
                        cont = 1



                    print(f"Habitació: {reserva}")
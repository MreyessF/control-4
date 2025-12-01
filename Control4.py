# Sistema de Reservas ByteCoffee (versión simple)

cupos_gamer = 3
cupos_estudio = 5

reservas_gamer = []
reservas_estudio = []

opcion = ""

def tiene_6_caracteres(nombre_cabina):
    return len(nombre_cabina) >= 6

while True:
    print("\n----BYTECOFFEE----")
    print("1) Reservar Cabina (GAMER O ESTUDIO)")
    print("2) Ver Disponibilidad de Cabinas")
    print("3) Liberar Cabinas")
    print("4) Salir")

    opcion = input("Seleccione opcion: ")

    # Para reservar las cabinas
    if opcion == "1":
        print("\n----MENU RESERVAR CABINA----")
        print("a. Reservar cabina zona Gamer")
        print("b. Reservar cabina zona Estudio")
        print("c. Volver al menu principal")

        op2 = input("Seleccione opción: ")

        # Reservar las cabinas de la zona gamer 
        if op2 == "a":
            if cupos_gamer == 0:
                print("No quedan cabinas en Zona Gamer.")
            else:
                print("\n--- Reservar en Zona Gamer ---")
                nombre_cabina = input("Nombre cabina: ")
                nombre_cliente = input("Nombre cliente: ")
                notebooks = input("Notebooks (s/n): ")

                # Guardamos datos simples
                reservas_gamer.append([nombre_cabina, nombre_cliente, notebooks])
                cupos_gamer -= 1
                print("Reserva registrada en Zona Gamer.")

        # Reservar las cabinas de la zona estudio
        elif op2 == "b":
            if cupos_estudio == 0:
                print("No quedan cabinas en Zona Estudio.")
            else:
                print("\n--- Reservar en Zona Estudio ---")
                nombre_cabina = input("Nombre cabina: ")
                nombre_cliente = input("Nombre cliente: ")
                notebooks = input("Notebooks (s/n): ")
                modalidad = input("Modalidad (s=Silenciosa / g=Grupal): ")

                reservas_estudio.append([nombre_cabina, nombre_cliente, notebooks, modalidad])
                cupos_estudio -= 1
                print("Reserva registrada en Zona Estudio.")

        elif op2 == "c":
            pass
        else:
            print("Opción inválida.")

    # Para ver la disponibilidad de las cabinas
    elif opcion == "2":
        print("\n--- DISPONIBILIDAD DE ZONAS ---")

        print("\nZONA GAMER (reservas):")
        if len(reservas_gamer) == 0:
            print("No hay reservas.")
        else:
            for r in reservas_gamer:
                print("Cabina:", r[0], "- Cliente:", r[1], "- Notebooks:", r[2])
        print("Cabinas disponibles:", cupos_gamer, "de 3")

        print("\nZONA ESTUDIO (reservas):")
        if len(reservas_estudio) == 0:
            print("No hay reservas")
        else:
            for r in reservas_estudio:
                print("Cabina:", r[0], "- Cliente:", r[1], "- Notebooks:", r[2], "- Modalidad:", r[3])
        print("Cabinas disponibles:", cupos_estudio, "de 5")

    # Aqui podemos liberar todas las cabinas que estan ocupadas
    elif opcion == "3":
        reservas_gamer = []
        reservas_estudio = []
        cupos_gamer = 3
        cupos_estudio = 5
        print("Todas las cabinas fueron liberadas.")

    # y por ultimo para salir del programa
    elif opcion == "4":
        print("Hasta pronto!")
        break

    else:
        print("Opción inválida.")
        
        
        
def tiene_mayusculas(nombre_cabina):
    return any(c.isupper() for c in nombre_cabina)

def tiene_6_caracteres(nombre_cabina):
    return len(nombre_cabina) >= 6
    
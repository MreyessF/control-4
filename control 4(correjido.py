# Sistema de Reservas ByteCoffee (versión simple)

cupos_gamer = 3
cupos_estudio = 5

reservas_gamer = []
reservas_estudio = []

opcion = ""


# validacion

def validar_cabina(nombre, lista):
    if len(nombre) < 6:
        return False
    if not any(c.isupper() for c in nombre):
        return False
    if not any(c.isdigit() for c in nombre):
        return False
    for reserva in lista:
        if nombre == reserva[0]:
            return False
    return True


def validar_cliente(nombre, lista):
    for r in lista:
        if nombre == r[1]:
            return False
    return True


def pedir_notebooks():
    notebooks = input("Notebooks (s/n): ").upper()
    while notebooks not in ["S", "N"]:
        print("ERROR: Solo se permite S o N.")
        notebooks = input("Notebooks (s/n): ").upper()
    return notebooks


def pedir_modalidad():
    modalidad = input("Modalidad (s=Silenciosa / g=Grupal): ").upper()
    while modalidad not in ["S", "G"]:
        print("ERROR: Solo se permite S o G.")
        modalidad = input("Modalidad (s=Silenciosa / g=Grupal): ").upper()
    return modalidad

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

        # Reservar cabinas GAMER
        if op2 == "a":
            if cupos_gamer == 0:
                print("No quedan cabinas en Zona Gamer.")
            else:
                print("\n--- Reservar en Zona Gamer ---")

                # VALIDAR CABINA
                nombre_cabina = input("Nombre cabina: ")
                while not validar_cabina(nombre_cabina, reservas_gamer):
                    print("ERROR: Cabina inválida (mínimo 6 caracteres, 1 mayúscula, 1 número y no repetida).")
                    nombre_cabina = input("Nombre cabina: ")

                # VALIDAR CLIENTE
                nombre_cliente = input("Nombre cliente: ")
                while not validar_cliente(nombre_cliente, reservas_gamer):
                    print("ERROR: Cliente ya tiene reserva.")
                    nombre_cliente = input("Nombre cliente: ")

                notebooks = pedir_notebooks()

                reservas_gamer.append([nombre_cabina, nombre_cliente, notebooks])
                cupos_gamer -= 1
                print("Reserva registrada en Zona Gamer.")

        # Reservar cabinas ESTUDIO
        elif op2 == "b":
            if cupos_estudio == 0:
                print("No quedan cabinas en Zona Estudio.")
            else:
                print("\n--- Reservar en Zona Estudio ---")

                # VALIDAR CABINA
                nombre_cabina = input("Nombre cabina: ")
                while not validar_cabina(nombre_cabina, reservas_estudio):
                    print("ERROR: Cabina inválida (mínimo 6 caracteres, 1 mayúscula, 1 número y no repetida).")
                    nombre_cabina = input("Nombre cabina: ")

                # VALIDAR CLIENTE
                nombre_cliente = input("Nombre cliente: ")
                while not validar_cliente(nombre_cliente, reservas_estudio):
                    print("ERROR: Cliente ya tiene reserva.")
                    nombre_cliente = input("Nombre cliente: ")

                notebooks = pedir_notebooks()
                modalidad = pedir_modalidad()

                reservas_estudio.append([nombre_cabina, nombre_cliente, notebooks, modalidad])
                cupos_estudio -= 1
                print("Reserva registrada en Zona Estudio.")

        elif op2 == "c":
            pass
        else:
            print("Opción inválida.")

    # Ver disponibilidad
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

    # Liberar cabinas
    elif opcion == "3":
        reservas_gamer = []
        reservas_estudio = []
        cupos_gamer = 3
        cupos_estudio = 5
        print("Todas las cabinas fueron liberadas.")

    elif opcion == "4":
        print("Hasta pronto!")
        break

    else:
        print("Opción inválida.")

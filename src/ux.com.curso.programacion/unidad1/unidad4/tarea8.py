def acceso():

    # Inicialización de variables
    intentos = 0
    clave_correcta = "1234"

    # Ciclo principal
    while intentos < 3:

        # Leer contraseña
        contrasena = input("Ingrese la contraseña: ")

        # Validar contraseña
        if contrasena == clave_correcta:
            print("Acceso Concedido")
            break
        else:
            intentos += 1
            print("Contraseña incorrecta")

    # Bloqueo de cuenta
    if intentos == 3:
        print("Cuenta bloqueada")


def main():
    acceso()


if __name__ == "__main__":
    main()
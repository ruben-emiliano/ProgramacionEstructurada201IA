def acumulado():
    # Inicialización de variables
    total_acumulado = 0
    semanas = 0
    meta = 2500

    # Ciclo que se repite mientras no se alcance la meta
    while total_acumulado < meta:

        # Leer salario semanal
        salario_semanal = float(input("Ingresa el salario de la semana: "))

        # Acumular salario
        total_acumulado = total_acumulado + salario_semanal

        # Incrementar contador de semanas
        semanas = semanas + 1

    # Mostrar resultado final
    print("Semanas trabajadas:", semanas)


def main():
    acumulado()


if __name__ == "__main__":
    main()
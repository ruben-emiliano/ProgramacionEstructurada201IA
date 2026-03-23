import math
w = 0
x = 0
z = 0

def solicitar_peso():
    global w
    w = float(input("Ingresa el peso de entrada (w): "))

def solicitar_dato():
    global x
    x = float(input("Ingresa el dato de entrada (x): "))

def calcular_activacion():
    global z
    z = w * x

def mostrar_resultado():
    print(f"Valor de activacion Z = {w} * {x} = {z}")
    print("(Resultado antes de pasar por la funcion no lineal)\n")

def estimar_activacion():
    print("=== Estimacion de Activacion de Neurona Artificial ===\n")

    for _ in iter(int, 1):
        solicitar_peso()
        solicitar_dato()
        calcular_activacion()
        mostrar_resultado()

        if input("¿Desea calcular otro valor? (s/n): ") != "s":
            print("Fin del programa.")
            break

def main():
    estimar_activacion()

if __name__ == "__main__":
    main()
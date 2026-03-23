import math

total_acumulado = 0
limite_seguridad = 2500

def solicitar_lote():
    global total_acumulado
    total_acumulado += float(input("Ingresa el tamaño del lote (MB): "))

def cargar_lote():
    print(f"Total acumulado en VRAM: {total_acumulado} MB")

def verificar_limite():
    if total_acumulado > limite_seguridad:
        print("Deteniendo carga inmediatamente para evitar error Out of Memory (OOM).")
        print(f"Total acumulado final: {total_acumulado} MB")

def simular_entrenamiento():
    print("ejercicio de simulacion de entrenamiento por lotes")
    print(f"Limite de seguridad VRAM: {limite_seguridad} MB\n")

    for _ in iter(int, 1):
        solicitar_lote()
        cargar_lote()

        if total_acumulado > limite_seguridad:
            verificar_limite()
            break

def main():
    simular_entrenamiento()

if __name__ == "__main__":
    main()
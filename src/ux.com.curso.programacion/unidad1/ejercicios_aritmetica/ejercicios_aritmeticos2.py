import math

#demosttrar el uso de las funciones de math

def mostar_funciones_math():
    #crear variable
    numero = 20

    #calcular la raiz cuadrada
    sen_x =math.sin(numero)
    cose_x =math.cos(numero)

    print("el seno de ",numero,"es:", sen_x)
    print("el coseno de ",numero,"es:", cose_x)

    resultado = sen_x **2 +cose_x **2
    print ("el resultado e sen 2^2(x)+ cos^2 es:", resultado)

def main():
    mostar_funciones_math()

if __name__ =="__main__":
    main

    
#calculo del radio de una esfera

import math

def esfera ():
    radio =float(input("ingrese el radio de la esfera en cm: "))
    volumen= (4/3) * math.pi * (radio **3)
    print("el volumen de la esfera es:", volumen, "cm cubicos")

def main():
    esfera()

if __name__ =="__main__":
    main()


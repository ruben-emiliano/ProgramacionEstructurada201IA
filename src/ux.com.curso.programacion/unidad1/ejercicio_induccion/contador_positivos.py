#desarrollo de algoritmos contador de positivos

#declaracion de variables
"""""
esta funcion lo que hace es que nos da una variable apartir de 0 que cada vez que se escribe un numero se va a sumar al resultado final
y una vez se escribe un numero 0< termina el contador 
"""""

def contador_positivos():
    contador =0
    while True:
        numero = int(input("ingrese un numero (-1 para terminar)"))
        if numero<0:
            break 
        contador += 1
    print("cantidad de numeros positivos ingresados: ", contador)

#definicion de la funcion main

"""""
llama a la funcion antes escrita
"""""
def main ():
    print("bienvenido al contador de positivos")
    contador_positivos()

#llamar a la funcion main para inicia el programa 
"""
llama a la funcion main
"""

if __name__=="__main__":
    main()
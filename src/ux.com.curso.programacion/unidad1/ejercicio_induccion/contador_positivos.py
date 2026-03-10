#desarrollo de algoritmos contador de positivos

#declaracion de variables

def contador_positivos():
    contador =0
    while True:
        numero = int(input("ingrese un numero (-1 para terminar)"))
        if numero<0:
            break 
        contador += 1
    print("cantidad de numeros positivos ingresados: ", contador)

#definicion de la funcion main
def main ():
    print("bienvenido al contador de positivos")
    contador_positivos()

#llamar a la funcion main para inicia el programa 
if __name__=="__main__":
    main()
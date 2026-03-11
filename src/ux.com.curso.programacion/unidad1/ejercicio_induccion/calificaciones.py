#asignacion de una letra en base a una calificacion 
def calificacion():
    numero_obtenido = float(input("ingrese la calificacion "))

    if numero_obtenido >=90:
        print("tu calificaion es A")
    
    elif numero_obtenido >=80 and numero_obtenido <90 :
        print("tu calificacion es B")
    
    elif numero_obtenido >=70 and numero_obtenido <80:
        print ("tu calificacion es C")
    elif numero_obtenido >=60 and numero_obtenido <70 :
        print("tu calificaion es D")
    elif numero_obtenido >=0 and numero_obtenido<60 :
        print("sacaste f")


def main():
    print("porcentaje de calificacion")
    calificacion()



if __name__ == "__main__":
    main()
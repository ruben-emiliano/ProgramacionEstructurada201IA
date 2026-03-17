#demostracion de tipos de dato en python 
def datos():
    entero = 25
    decimal = 3.14
    cadena = "hola, mundo"
    booleano = True

    print(entero)
    print(decimal)
    print(cadena)
    print(booleano)
def tipo_datos_compuestos():
    lista=[10,20,30,40]
    tupla=(19,29,39,49)
    diccionario={"nombre":"juan","edad":30,"ciudad":"madrid"}

    print(lista)
    print(tupla)
    print(diccionario)
def main():
    datos()

if __name__ == "__main__":
    main()

"""
fondo de ahorro 
"""

def ahorro ():
    saldo=0
    meta=1000
    while saldo<=meta:
        deposito =int(input("ingrese el deposito actual: "))
        saldo+=deposito
    return saldo

def main():
    resultados=ahorro()
    print("meta superada $", resultados)

if __name__=="__main__":
    main()
    
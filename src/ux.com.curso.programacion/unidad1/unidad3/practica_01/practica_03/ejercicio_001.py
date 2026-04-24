def mes ():
    mes =int(input("ingresa tu mes"))
    return mes


def dia ():
    dia= int(input("ingresa tu dia"))
    return dia

def año():
    año=int(input("ingresa tu año"))
    return año

def fecha (año, mes, dia):
    if mes < 1 or mes > 12:
        return False
    
    if dia <1 or dia >12:
        return False
    
    if mes in 

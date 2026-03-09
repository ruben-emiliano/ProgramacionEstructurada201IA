numero_horas = float(input("ingrese el numero de horas trabajadas:"))
tarifa_hora = float(input("ingrese la tarifa por hora:"))
nombre_empleado = input("ingrese el nombre del empleado:")

#las horas mayores a 35 se pagan como superiores

if numero_horas >35:
    horas_extras = numero_horas-35
    pago_bruto = (35 * tarifa_hora) + (horas_extras *tarifa_hora * 1.5)
else:
    pago_bruto=numero_horas * tarifa_hora


#claculo de impuestos 
if pago_bruto <= 2000:
    impuesto = 0
elif pago_bruto <=2200:
    impuesto = (pago_bruto -2000) *0.20
else:
    impuesto =(pago_bruto -2220) *0.30+220*0.20

pago_neto = pago_bruto - impuesto

#mostrar resultado 
print(f"empleado: {nombre_empleado}")
print(f"pago bruto: ${pago_bruto:.2f}")
print(f"impuestos: ${impuesto:.2f}")
print(f"pago_neto: ${pago_neto:.2f}")

    

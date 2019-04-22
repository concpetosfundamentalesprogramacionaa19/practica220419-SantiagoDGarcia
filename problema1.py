import sys


costo1 = input ("ingrese el costo de cada hora del empleado:")
hora = 100


valor = (hora * float(costo1))
print ("valor", valor)
descuento = (valor*0.10)
sueldo = (valor-descuento)

print ("valor mensual a pagar %d\nvalor de descuento de seguro %d\nsueldo mensual %d"  % (valor, descuento, sueldo))




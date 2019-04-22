#problema2

x = input("ingrese el valor de x:")#entrada de datos
y = input("ingrese el valor de y:")
z = input("ingrese el valor de z:")



#se transforma de formato string por defecto a float, para poder realizar la operacion


m = (float(x)+(float(y)/float(z)))/(float(x)-(float(y)/float(z)))#formula de resolucion


print("El valor de m es:\nx = %s\n\ty = %s\n\t\tz = %s\nda como resultado: \n\t\t\t%s"  %  (x, y, z, m))#resultado

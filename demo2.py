""""
	archivo: demo2.py
	Ejemplo de lenguaje Python
	autor:@SantiagoDGarcia
"""

import sys

nombre_archivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]

suma = int(valor1) + int(valor2) #suma de varibles
multiplicacion = int(valor1) * int(valor2)# multiplicacion de variables


print("la suma es:  %d"    % suma)#resultados
print("la multiplicacion es:  %d"    % multiplicacion)
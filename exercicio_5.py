#!/usr/bin/python3

numeros = [2, 53, 38, 40, 87, 12, 55, 34]
pares = []
impares = []

for x in numeros:
	if x % 2 == 0:
		pares.append(x)
	else:
		impares.append(x)	

print (pares)
print (impares)



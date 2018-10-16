#!/usr/bin/python3

x = 0
n = 0
numero = 0

while x < 5:
	n = float(input('\nDigite um úmero:' ))
	numero = numero + n
	x = x + 1

media = (numero/5)

print ('\nA média dos números digitados é', media)

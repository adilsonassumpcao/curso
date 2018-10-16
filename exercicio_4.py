#!/usr/bin/python3

N1,N2,N3 = 0,0,0

N1 = float(input('\nDigite o primeiro número:' ))
N2 = float(input('\nDigite o segundo número:' ))
N3 = float(input('\nDigite o terceiro número:' ))

if N1 >= N2 and N1 >= N3:
	print ('O primeiro número é o maior:', N1)

if N2 >= N3:
	print ('O segundo número é o maior:', N2)
else:
	print ('O terceiro número é o maior:', N3)
 	
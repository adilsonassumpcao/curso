#!/usr/bin/python3

palavra = str(input('Digite uma palavra:'))
vogais = 'aeiouAEIOU'

cont = 0

for x in palavra:
	if x not in vogais:
		cont = cont + 1


print('Na palavra:', palavra, 'existem:', cont, 'consoantes.')


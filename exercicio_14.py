#!/usr/bin/python3

#Usando o Raise do Try.

try:
	linguagem = input('Qual a linguagem de progamação?\n')

#Método lower() deixa toda a string minúscula.
#Método upper() deixa toda a string maiúscula.
#Método strip() tira todos os espaços em branco de dentro da string.
#Método title() deixa a primeira letra da string maiúscula.

	if linguagem.lower().strip() != 'Python':
		raise ValueError('Linguagem Errada')

except ValueError as e:
	print (e)
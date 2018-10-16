#!/usr/bin/python3

'''
def soma(x,y):
	return x + y

def sub(x,y):
	return x - y

def mul(x,y):
	return x * y

def div(x,y):
	return x / y

numero_1 = int(input('Digite um número:'))
numero_2 = int(input('Digite um número:'))

resultado = soma(numero_1,numero_2)
print ('O resultado da soma é:', resultado)
'''

import sys

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = 3

def criptografar(message):
	novo = ''
	for c in message:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo += alfabeto[(indice + chave) % len(alfabeto)]

		else:
			novo += c	
	print (novo)
	

def decriptografar(message):
	novo = ''
	for c in message:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo += alfabeto[(indice - chave) % len(alfabeto)]

		else:
			novo += c	
	print (novo)

def main():
	#Capturar 2 argumentos da linha de comando, antes mesmo de executar o programa em si.
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	# print (command,message,sep='\n')

	#Opção número 1

	# if command == 'cript':
	# 	criptografar(message)
	# elif command == 'decript':
	# 	decriptografar(message)
	# else:
	# 	print ('Comando Inválido')

	#Opção número 2

	opcoes = {'cript' : criptografar, 'decript' : decriptografar}

	opcoes[command] (message)

if __name__ == '__main__':
	main()



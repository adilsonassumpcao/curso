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

def criptografar():
	print ('Qualquer coisa')

def main():
	#Capturar 2 argumentos da linha de comando
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	print (command,message,sep='\n')

	if command == 'teste':
		criptografar()

if __name__ == '__main__':
	main()



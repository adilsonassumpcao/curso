#!/usr/bin/python3

import sys

def soma(x,y):
	total = x + y
	return total

def sub(x,y):
	total = x - y
	return total

def mul(x,y):
	total = x * y
	return total

def div(x,y):
	total = x / y
	return total

def main():
	#Solicita 2 números do usuário e a operação que o usuário quer efetuar com os números.
	numero_1 = float(input('1º - Número:' ))
	numero_2 = float(input('2º - Número:' ))
	operacao = input('Operação:')

	if operacao == '+':
		print ('O resultado da soma é:', soma(numero_1, numero_2))
	elif operacao == '-':
		print ('O resultado da subtração é:', sub(numero_1, numero_2))
	elif operacao == '*':
		print ('O resultado da multiplicação é:', mul(numero_1, numero_2))	
	elif operacao == '/':
		print ('O resultado da divisão é:', div(numero_1, numero_2))
	else:
		print('Operador Inválido')	

if __name__ == '__main__':
	main()
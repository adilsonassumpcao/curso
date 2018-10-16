#!/usr/bin/python3

#Tratando erros

while True:
	try:
		x = int (input('Digite um número: '))
		y = int (input('Digite um número: '))
	
		print (x + y)

	except Exception as e:
		print ('Digite apenas números')
	else:
		pass
	finally:
		print ('finally')
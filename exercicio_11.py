#!/usr/bin/python3


#Usando o else do laço for

nomes = ['joao','maria', 'paulo', 'joana']

s = input('Buscar por nome:' )

for nome in nomes:
	if s == nome:
		print ('Está na lista')
		break

else:
	print ('Não está na lista')
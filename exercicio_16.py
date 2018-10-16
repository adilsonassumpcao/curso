#!/usr/bin/python3

nomes = ['Yasmin', 'Rafael', 'Jéssica']

#Forma 1 para criar um arquivo, ler uma lista e escrever os nomes dessa lista no arquivo.

with open('nomes.tx', 'a') as f:
	for nome in nomes:
		f.write(nome + '\n')

#Forma 2 para criar um arquivo, ler uma lista e escrever os nomes dessa lista no arquivo.

with open('nomes-2.txt', 'a') as f:
	f.writelines([x + '\n' for x in nomes])

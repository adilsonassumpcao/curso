#!/usr/bin/python3

from datetime import datetime

#Programa de exemplo para abertura de arquivo.

# Método x abre um arquivo com um determinado nome, caso ele ainda não exista na pasta.
# Método w sobrescreve tudo que está dentro do arquivo.
# Método a adiciona sempre uma linha no final do arquivo.
# Método r faz a leitura do arquivo.

try:
	with open('nomes', 'x') as f:
		f.write('\n\nLISTA DE NOMES\n')
		f.write('\t\n\nAdilson\n')
		f.write('\t\n\nAntonio\n')
		f.write('\t\n\nMaria\n')
		f.write('\t\n\nJoão\n')
		f.write('\t\n\nMarta\n')
		f.write('\t\n\nLuis\n')

#FileExistError trata um erro quando um arquivo já existe.

except FileExistsError as e:
	with open('log', 'a') as f:
		#f.write('\tOlá\n\tOi\n\n'.format(e))

# O comando abaixo grava no meu arquivo o log dos erros do except.
		f.write('{}\n'.format(e))
	
#Método para abertura de arquivo sem usar o with open.
#Obs.: Não esquecer de fechar o arquivo, que é obrigatório nesse caso.

# f = open('teste.txt', 'w')
# f.write('curso python')
# f.close()
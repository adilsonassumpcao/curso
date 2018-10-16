#!/usr/bin/python3

convidados = ['Daniel', 'Maria', 'Adilson']

try:

	pos = int(input('Digite a posição do convidado: '))
	print (convidados[pos])


#ValueError é para tratar erros com valores digitados (Se o usuário digitar algo diferente do tipo de entrada que o sistema está pedindo).

except ValueError:
	print ('Digite apenas números')


#IndexError é para tratar erros de indices.

except IndexError:
 	print ('A lista tem {} convidados apenas'.format(len(convidados)))


#Exception é para tratar erros genéricos.

except Exception as e:
	print(e)




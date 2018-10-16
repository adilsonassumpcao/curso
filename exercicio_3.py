#!/usr/bin/python3

N1,N2,N3,N4 = 0,0,0,0

Nome = str(input('\nDigite o nome do aluno:'))
N1 = float(input('\nDigite a primeira nota do aluno:' ))
N2 = float(input('\nDigite a segunda nota do aluno:' ))
N3 = float(input('\nDigite a terceira nota do aluno:' ))
N4 = float(input('\nDigite a quarta nota do aluno:' ))
print ('\n')

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 + 1))/10

if media >= 7.0:
	print (Nome, 'sua média é:', media)
	print ('Você está Aprovado!!!\n')

elif media >= 5.0 and media <= 6.9:
	print (Nome, 'sua média é:', media, 'vocẽ está de exame.\n')
	nota_exame = float(input('Digite a nota do seu exame:'))
	media_exame = (media + nota_exame) / 2

if media_exame >= 7.0:
	print (Nome, 'você foi aprovado no exame!!!')
else:
	print (Nome, 'vocẽ foi reprovado no exame!!!')



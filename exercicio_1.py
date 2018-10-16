#!/usr/bin/python3

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 110:
	print('Você foi multado em R$:', (velocidade-110)*5)
else:
	print('Velocidade do carro dentro do permitido!')

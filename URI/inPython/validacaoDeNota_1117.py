#coding: utf-8


def ehValido(x):
	if 0 <=  x <= 10: return True
	else: return False

cont = 0
soma = 0
while cont < 2:
	x = float(input())

	if ehValido(x):
		cont += 1
		soma += x

	else: print('nota invalida')

print('media = %.2f' %(soma/2))

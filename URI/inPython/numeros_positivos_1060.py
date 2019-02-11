#coding: utf-8

'''ler 6 numeros e determinar quantos são positivos'''

cont = 0

for i in range(6):
	x = float(input())
	if x > 0:
		cont += 1

print('{:d} valores positivos'.format(cont))
#coding: utf-8

numero_de_pares = 0

for i in range(5):
	x = float(input())

	if x % 2 == 0:
		numero_de_pares += 1
		


print('{:d} valores pares'.format(numero_de_pares))

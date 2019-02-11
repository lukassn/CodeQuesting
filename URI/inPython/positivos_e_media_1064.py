#coding: utf-8


numero_de_positivos = 0
soma_de_positivos = 0

for i in range(6):
	x = float(input())

	if x > 0:
		numero_de_positivos += 1
		soma_de_positivos += x

print('{:d} valores positivos\n{:.1f}'.format(numero_de_positivos, (soma_de_positivos)/numero_de_positivos))

#coding: utf-8

pares = 0
impares = 0
positivos = 0
negativos = 0


for i in range(5):
	x = float(input())

	if x % 2 == 0:
		pares += 1

	elif x % 2 != 0:
		impares += 1

	if x > 0:
		positivos += 1

	elif x < 0:
		negativos += 1


print('{:d} valor(es) par(es)'.format(pares))
print('{:d} valor(es) impar(es)'.format(impares))
print('{:d} valor(es) positivo(s)'.format(positivos))
print('{:d} valor(es) negativo(s)'.format(negativos))

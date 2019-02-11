#coding: utf-8

def listarNumerosEntre(x, y):
	if x > y :
		a = x
		x = y
		y = a

	lista = []

	while x <= y:
		lista.append(x)
		x += 1
	return lista

while True:
	x, y = map(int, input().split())

	if x <= 0 or y <= 0: break

	soma = 0
	lista = listarNumerosEntre(x,y)
	saida = ''
	for i in range(len(lista)):
		soma += int(lista[i])
		saida += str(lista[i]) + ' '
	print('%sSum=%d' %(saida, soma))
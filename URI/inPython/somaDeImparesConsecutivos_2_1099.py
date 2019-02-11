#coding: utf-8

def somaImparesEntre(x, y):
	if x > y :
		a = x
		x = y
		y = a

	soma_impares = 0

	while x < y-1:
		x += 1
		if x % 2 != 0:
			soma_impares += x

	return soma_impares

for i in range(int(input())):
	x, y = map(int, input().split())
	print(somaImparesEntre(x,y))
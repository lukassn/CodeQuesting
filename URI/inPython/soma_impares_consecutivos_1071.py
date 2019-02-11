#coding: utf-8

x = int(input())
y = int(input())

if x > y :
	a = x
	x = y
	y = a

soma_impares = 0

while x < y-1:
	x += 1
	if x % 2 != 0:
		soma_impares += x

print(soma_impares)
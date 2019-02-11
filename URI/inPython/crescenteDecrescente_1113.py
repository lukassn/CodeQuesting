#coding: utf-8

while True:
	x,y = map(int, input().split())

	if x == y: break
	if x > y:
		print('Decrescente')
	elif x < y:
		print('Crescente')
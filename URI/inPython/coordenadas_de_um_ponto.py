#coding: utf-8

enter = input().split()

x, y = map(float, enter)

if x == y == 0:
	print('Origem')

if x == 0 and (y > 0 or y < 0):
	print('Eixo y')

if (x > 0 or x < 0) and y == 0:
	print('Eixo x')

if x > 0 and y > 0:
	print ('Q1')

if x < 0 and y > 0:
	print('Q2')

if x < 0 and y < 0:
	print('Q3')

if x > 0 and y < 0:
	print('Q4')


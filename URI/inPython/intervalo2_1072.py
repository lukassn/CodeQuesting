#coding: utf-8

x = int(input())

IN = 0
OUT = 0

for i in range(x):
	n = int(input())

	if n >= 10 and n <= 20:
		IN += 1

	else:
		OUT += 1

print('{:d} in\n{:d} out'.format(IN, OUT))
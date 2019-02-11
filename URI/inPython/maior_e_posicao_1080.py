#coding: utf-8


maior = 0
pos = 0
for i in range(100):
	x = int(input())
	
	if x > maior:
		maior = x
		pos = i+1
	
print('%d\n%d' % (maior, pos))

#coding: utf-8

'''
Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %
'''

coelhos = 0
ratos = 0
sapos = 0

for i in range(int(input())):
	qtd, animal = input().split()

	if animal == 'C':
		coelhos += int(qtd)

	elif animal == 'R':
		ratos += int(qtd)

	elif animal == 'S':
		sapos += int(qtd)

total = (coelhos+sapos+ratos)

print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % coelhos)
print('Total de ratos: %d' % ratos)
print('Total de sapos: %d' % sapos)
print('Percentual de coelhos: {:.2f} %'.format(100*coelhos/total))
print('Percentual de ratos: {:.2f} %'.format(100*ratos/total))
print('Percentual de sapos: {:.2f} %'.format(100*sapos/total))

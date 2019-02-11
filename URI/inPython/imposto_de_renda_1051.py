#coding: utf-8

x = float(input())

if x <= 2000:
	print('Isento')

	
elif x > 2000:

	imposto = 0

	if x > 4500:
		valor = x - 2000
		imposto += 1000*0.08
		valor = valor - 1000
		imposto += 1500 * 0.18
		valor = valor - 1500
		imposto += valor * 0.28
		

	if 3000 < x <= 4500:
		valor = x - 2000
		imposto += 1000*0.08
		valor = valor - 1000
		imposto += valor * 0.18
		

	if 2000 < x <= 3000:
		valor = x - 2000
		imposto += valor*0.08
		
	
	print('R$ {:.2f}'.format(imposto))


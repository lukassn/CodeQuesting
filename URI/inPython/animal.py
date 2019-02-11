#coding: utf-8

re = input()
fi = input()
co = input()

if re == 'vertebrado':
	if fi == 'ave':
		if co == 'carnivoro':
			print('aguia')
		if co == 'onivoro':
			print('pomba')

	if fi == 'mamifero':
		if co == 'onivoro':
			print('homem')

		if co == 'herbivoro':
			print('vaca')

if re == 'invertebrado':
	if fi == 'inseto':
		if co == 'hematofago':
			print('pulga')
		if co == 'herbivoro':
			print('lagarta')

	if fi == 'anelideo':
		if co == 'hematofago':
			print('sanguessuga')

		if co == 'onivoro':
			print('minhoca')
#coding: utf-8

enter = float(input())

def intervalo(entrada):

	output = 'Intervalo '
	if entrada < 0:
		output = 'Fora de intervalo'

	elif entrada >= 0 and entrada <= 25.0000:
		output += '[0,25]'

	elif entrada > 25.0000 and entrada <= 50.0000:
		output += '(25,50]'

	elif entrada > 50.0000 and entrada <= 75.0000:
		output += '(50,75]'

	elif entrada > 50.0000 and entrada <= 100.0000:
		output += '(75,100]'

	return output

print(intervalo(enter))

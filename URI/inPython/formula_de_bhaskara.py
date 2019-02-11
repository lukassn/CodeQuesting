#coding: utf-8

enter = input().split()

a = float(enter[0])
b = float(enter[1])
c = float(enter[2])


def bhaskara(a, b, c):
	output = ''
	
	if a == 0:
		output = 'Impossivel calcular'

	else:
		delta = b**2 - 4*a*c
		x1 = ((-b) + delta**(1/2))/(2*a)
		x2 = ((-b) - delta**(1/2))/(2*a)


		if delta < 0:
			output = 'Impossivel calcular'

		elif delta == 0 and x1 == x2:
			output = "R1 = %.5f\nR2 = %.5f" % (x1)
				
		else:
			output = "R1 = %.5f\nR2 = %.5f" % (x1, x2)

	return output

print(bhaskara(a,b,c))
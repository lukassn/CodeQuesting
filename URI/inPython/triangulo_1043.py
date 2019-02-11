#coding: utf-8

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

a, b, c = map(float, input().split())

def ehTriangulo(a, b, c):
	
	if abs((b-c)) < a and a < (b+c) and abs((a-c)) < b and b < (a+c) and abs((a-b)) < c and c < (a+b):
		return True

	else: return False


if ehTriangulo(a, b, c) == True:
	print("Perimetro = {:.1f}".format((a + b + c)))

if ehTriangulo(a, b, c) == False:
	area = (a+b)*c/2
	print("Area = {:.1f}".format(area))

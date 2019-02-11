#coding: utf-8

def insertionsort(A):

    for j in range(1,len(A)):
        key = A[j]

        i = j-1
        
        while (i > -1) and key < A[i]:
            A[i+1]=A[i]
            i=i-1
        
        A[i+1] = key
    return A

enter = input().split()

for i in range(len(enter)):
	enter[i] = float(enter[i])

insertionsort(enter)
a, b, c = enter[2], enter[1], enter[0]

saida = []

if a >= (b+c):
	print("NAO FORMA TRIANGULO")

else:

	if ((a**2) == (b**2 + c**2)):
		print("TRIANGULO RETANGULO")

	if a**2 > (b**2 + c**2):
		print("TRIANGULO OBTSANGULO")

	if a**2 < (b**2 + c**2):
		print("TRIANGULO ACUTANGULO")

	if a == b or a == c or b == c:
		if a == b == c:
			print("TRIANGULO EQUILATERO")
		
		else:
			print("TRIANGULO ISOSCELES")
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

n1, n2, n3 = map(int, input().split())
sequencia_inicial = [n1, n2, n3]
sequencia_crescente = sequencia_inicial
insertionsort(sequencia_crescente)

sequencia_inicial = [n1, n2, n3]
for i in sequencia_crescente:
	print(i)
print()

for i in sequencia_inicial:
	print(i)
print()
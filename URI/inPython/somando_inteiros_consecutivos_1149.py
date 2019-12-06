#coding: utf-8

enter = input().split()
a = int(enter[0])
n = 0
for i in range(1,len(enter)):
    if  int(enter[i]) > 0: n = int(enter[i])

soma = 0
for i in range(n):
    soma += a + i

print(soma)

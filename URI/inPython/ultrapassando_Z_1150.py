#coding: utf-8

cont = 1
x = int(input())
soma = x
z = 0
while(z <= x):
    z = int(input())

for i in range(x, z + 1):
    if soma <= z:
        cont += 1
        soma += i
print(cont)

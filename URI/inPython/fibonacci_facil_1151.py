#coding: utf-8

n = int(input())

cont = 0
a = 0
b = 1
s =[]
while (cont < n):
    cont += 1
    s.append(str(a))
    c = a
    a = b
    b = a + c

s = ' '.join(s)
print(s)

# coding: utf-8

n = int(input())
cont = 0
while(cont < n):
    cont += 1
    c = 0
    x = int(input())
    y = 0
    while (c < x):
        c += 1
        if x % c == 0 and x != c:
            y += c
    if x == y: print("%d eh perfeito" % x)
    else: print("%d nao eh perfeito" % x)


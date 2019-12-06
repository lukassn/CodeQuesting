#coding: utf-8

n = int(input())

a, b, c, x, y = 0, 1, 0, 0, 0

for i in range(n*2):

    if x % 2 == 1: # impar
        y += 2
        b += 1
        c += 1

    else:  # par
        a += 1
        b += y
        c = a * b

    x += 1
    print(a,b,c)


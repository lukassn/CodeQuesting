#coding: utf-8

n = int(input())

cont = 0
while(cont < n):
    cont += 1
    x, y = map(int, input().split())
    s = 0
    c = 0
    while(c < y):
        if x % 2 == 1:
            s += x
            c += 1
        print(x,s)
        x += 1
    print(s)

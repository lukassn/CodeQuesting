#coding: utf-8

cont = 0
while(True):
    n = int(input())
    if n == 0: break
    cont += 1
    s = 0
    c = 0
    while(c < 5):
        if n % 2 == 0:
            s += n
            c += 1
        n += 1
    print(s)

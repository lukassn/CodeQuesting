#coding: utf-8

cont = 0
while(cont < 10):
    n = int(input())
    if n <= 0: print("X[%d] = 1" % cont)
    else: print("X[%d] = %d" % (cont, n))
    cont += 1


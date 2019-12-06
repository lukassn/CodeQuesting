#coding utf-8

n = int(input())
cont = 0

def ehPrimo(x):
    e = False
    y = 0
    for i in range(1, x+1):
        if x % i == 0: y += 1
    if y == 2: e = True
    return e

while(cont < n):
    cont += 1
    x = int(input())
    if ehPrimo(x): print("%d eh primo" % x)
    else: print("%d nao eh primo" % x)
